from locust import task

from clients.http.gateway.locust import GatewayHTTPTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from tools.locust.user import LocustBaseUser


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    """
    Нагрузочный TaskSet: создание пользователя, открытие депозита, список счетов.
    Задачи в произвольном порядке; open_deposit_account и get_accounts зависят от shared state.
    """

    create_user_response: CreateUserResponseSchema | None = None

    @task(2)
    def create_user(self) -> None:
        """Создание пользователя; результат сохраняется для open_deposit_account и get_accounts."""
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self) -> None:
        """Открытие депозитного счёта только если пользователь уже создан."""
        if not self.create_user_response:
            return
        self.accounts_gateway_client.open_deposit_account(self.create_user_response.user.id)

    @task(6)
    def get_accounts(self) -> None:
        """Список счетов пользователя только при наличии созданного пользователя."""
        if not self.create_user_response:
            return
        self.accounts_gateway_client.get_accounts(self.create_user_response.user.id)


class GetAccountsScenarioUser(LocustBaseUser):
    """Виртуальный пользователь Locust с HTTP-сценарием GetAccountsTaskSet."""

    tasks = [GetAccountsTaskSet]
