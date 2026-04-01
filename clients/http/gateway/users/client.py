from typing import TypedDict

from httpx import Response, Client

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

# users_client = UsersGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))
