from locust import events, task

from clients.http.gateway.locust import GatewayHTTPTaskSet
from seeds.schema.result import SeedUserResult, SeedsResult
from seeds.scenarios.existing_user_get_operations import ExistingUserGetOperationsSeedsScenario
from tools.locust.user import LocustBaseUser


class GetOperationsTaskSet(GatewayHTTPTaskSet):
    """
    Нагрузочный TaskSet для существующего пользователя:
    - список счетов;
    - список операций;
    - агрегированная статистика по операциям.
    """

    seeds_result: SeedsResult | None = None
    seed_user: SeedUserResult | None = None
    account_id: str | None = None

    def on_start(self) -> None:
        """
        Инициализирует API-клиенты и выбирает случайного пользователя
        из подготовленных сидингом данных.
        """
        super().on_start()

        if not self.__class__.seeds_result:
            seeds_scenario = ExistingUserGetOperationsSeedsScenario()
            self.__class__.seeds_result = seeds_scenario.load()

        self.seed_user = self.__class__.seeds_result.get_random_user()
        if self.seed_user.credit_card_accounts:
            self.account_id = self.seed_user.credit_card_accounts[0].account_id

    @task(2)
    def get_accounts(self) -> None:
        """Получает список счетов существующего пользователя."""
        if not self.seed_user:
            return
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(5)
    def get_operations(self) -> None:
        """Получает список операций по выбранному счёту."""
        if not self.account_id:
            return
        self.operations_gateway_client.get_operations(account_id=self.account_id)

    @task(3)
    def get_operations_summary(self) -> None:
        """Получает агрегированную статистику по операциям счёта."""
        if not self.account_id:
            return
        self.operations_gateway_client.get_operations_summary(account_id=self.account_id)


@events.test_start.add_listener
def prepare_existing_user_get_operations_seeds(environment, **kwargs) -> None:
    """
    Подготавливает сидинг до старта нагрузки.
    Если дамп уже существует, используется он; иначе выполняется build.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    try:
        GetOperationsTaskSet.seeds_result = seeds_scenario.load()
    except FileNotFoundError:
        seeds_scenario.build()
        GetOperationsTaskSet.seeds_result = seeds_scenario.load()


class GetOperationsScenarioUser(LocustBaseUser):
    """Виртуальный пользователь Locust, исполняющий GetOperationsTaskSet."""

    tasks = [GetOperationsTaskSet]
