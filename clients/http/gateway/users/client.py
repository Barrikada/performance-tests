import time
from typing import Any, TypedDict

from httpx import Client, Response

from clients.http.client import HttpClient


class CreateUserRequestDict(TypedDict):
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str

class UsersGatewayHTTPClient(HttpClient):
    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post(f"/api/v1/users", json=request)

    def create_user(self) -> dict[str, Any]:
        request = CreateUserRequestDict(
            email=f"user.{time.time()}@example.com",
            lastName="string",
            firstName="string",
            middleName="string",
            phoneNumber="string",
        )
        response = self.create_user_api(request)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))
