from typing import TypedDict

from httpx import Client, Response

from clients.http.client import HttpClient


class CreateVirtualCardRequestDict(TypedDict):
    """
    Структура тела запроса для выпуска виртуальной карты.

    :param userId: идентификатор пользователя
    :param accountId: идентификатор аккаунта
    """
    userId: str
    accountId: str


class CreatePhysicalCardRequestDict(TypedDict):
    """
    Структура тела запроса для выпуска физической карты.

    :param userId: идентификатор пользователя
    :param accountId: идентификатор аккаунта
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HttpClient):
    def issue_virtual_card_api(self, request: CreateVirtualCardRequestDict) -> Response:
        """
        Выполняет запрос на выпуск виртуальной карты.

        :param request: тело запроса с данными пользователя
        :return: объект Response с данными ответа от сервера
        """
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreatePhysicalCardRequestDict) -> Response:
        """
        Выполняет запрос на выпуск физической карты.

        :param request: тело запроса с данными пользователя
        :return: объект Response с данными ответа от сервера
        """
        return self.post(f"/api/v1/cards/issue-physical-card", json=request)

    def issue_physical_card(self, user_id: str, account_id: str) -> dict:
        """
        Выпуск физической карты для указанного пользователя и счёта.

        :param user_id: Идентификатор пользователя.
        :param account_id: Идентификатор счёта.
        :return: Распарсенный JSON-ответ с данными карты.
        """
        request = CreatePhysicalCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_physical_card_api(request)
        return response.json()


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))
