from typing import TypedDict

from httpx import Response

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
