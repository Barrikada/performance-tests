from typing import TypedDict

from httpx import Client, Response

from clients.http.client import HttpClient


class DocumentDict(TypedDict):
    """
    Описание структуры документа (ссылка и текстовое содержимое).
    """
    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа получения документа тарифа.
    """
    tariff: DocumentDict


class GetContractDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа получения документа контракта.
    """
    contract: DocumentDict


class DocumentsGatewayHTTPClient(HttpClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получить документ тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: JSON-ответ с данными документа тарифа.
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получить документ контракта по счету.

        :param account_id: Идентификатор счета.
        :return: JSON-ответ с данными документа контракта.
        """
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))
