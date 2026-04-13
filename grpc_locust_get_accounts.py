from locust import User, between, task

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    Нагрузочный TaskSet: создание пользователя, открытие депозита, список счетов (gRPC).
    """

    create_user_response: CreateUserResponse | None = None

    @task(2)
    def create_user(self) -> None:
        """Создание пользователя через UsersGatewayGRPCClient; ответ хранится в shared state."""
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self) -> None:
        """Открытие депозитного счёта только при наличии user_id из ответа create_user."""
        if not self.create_user_response:
            return
        user_id = self.create_user_response.user.id
        self.accounts_gateway_client.open_deposit_account(user_id)

    @task(6)
    def get_accounts(self) -> None:
        """Список счетов только если пользователь уже создан (есть user_id)."""
        if not self.create_user_response:
            return
        user_id = self.create_user_response.user.id
        self.accounts_gateway_client.get_accounts(user_id)


class GetAccountsScenarioUser(User):
    """Виртуальный пользователь Locust с gRPC-сценарием GetAccountsTaskSet."""

    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1, 3)
