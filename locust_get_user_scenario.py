from locust import User, between, task

from clients.grpc.gateway.users.client import (
    UsersGatewayGRPCClient,
    build_users_gateway_locust_grpc_client,
)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class GetUserScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayGRPCClient
    create_user_response: CreateUserResponse

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь создаём пользователя через gRPC UsersGatewayService.CreateUser.
        """
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def get_user(self) -> None:
        """
        Основная нагрузочная задача: получение информации о пользователе по gRPC GetUser.
        """
        self.users_gateway_client.get_user(self.create_user_response.user.id)
