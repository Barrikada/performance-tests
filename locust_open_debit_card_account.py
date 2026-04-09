from locust import User, between, task

from clients.http.gateway.accounts.client import (
    AccountsGatewayHTTPClient,
    build_accounts_gateway_locust_http_client,
)
from clients.http.gateway.users.client import (
    UsersGatewayHTTPClient,
    build_users_gateway_locust_http_client,
)
from clients.http.gateway.users.schema import CreateUserResponseSchema


class OpenDebitCardAccountScenarioUser(User):
    """
    Нагрузочный сценарий: создание пользователя и открытие дебетового счёта через HTTP API-клиенты.
    """

    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        """
        Вызывается один раз на виртуального пользователя: инициализация клиентов и создание пользователя.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self) -> None:
        """
        Нагрузочная задача: открытие дебетового счёта для пользователя из on_start.
        """
        self.accounts_gateway_client.open_debit_card_account(
            self.create_user_response.user.id,
        )
