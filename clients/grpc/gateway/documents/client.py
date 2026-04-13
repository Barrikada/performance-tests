from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest,
    GetContractDocumentResponse,
)
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest,
    GetTariffDocumentResponse,
)


class DocumentsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с DocumentsGatewayService.
    Предоставляет высокоуровневые методы для работы с документами.
    """

    def __init__(self, channel: Channel) -> None:
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к DocumentsGatewayService.
        """
        super().__init__(channel)

        self.stub: DocumentsGatewayServiceStub = DocumentsGatewayServiceStub(channel)

    def get_tariff_document_api(self, request: GetTariffDocumentRequest) -> GetTariffDocumentResponse:
        """
        Низкоуровневый вызов метода GetTariffDocument через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными документа тарифа.
        """
        return self.stub.GetTariffDocument(request)

    def get_contract_document_api(self, request: GetContractDocumentRequest) -> GetContractDocumentResponse:
        """
        Низкоуровневый вызов метода GetContractDocument через gRPC.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ от сервиса с данными документа контракта.
        """
        return self.stub.GetContractDocument(request)

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponse:
        """
        Тарифный документ по идентификатору счёта.

        :param account_id: Идентификатор счёта.
        :return: Ответ GetTariffDocumentResponse.
        """
        request: GetTariffDocumentRequest = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponse:
        """
        Договорной документ по идентификатору счёта.

        :param account_id: Идентификатор счёта.
        :return: Ответ GetContractDocumentResponse.
        """
        request: GetContractDocumentRequest = GetContractDocumentRequest(account_id=account_id)
        return self.get_contract_document_api(request)


def build_documents_gateway_grpc_client() -> DocumentsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра DocumentsGatewayGRPCClient.

    :return: Инициализированный клиент для DocumentsGatewayService.
    """
    return DocumentsGatewayGRPCClient(channel=build_gateway_grpc_client())


def build_documents_gateway_locust_grpc_client(environment: Environment) -> DocumentsGatewayGRPCClient:
    """
    Создаёт DocumentsGatewayGRPCClient для нагрузочного тестирования в Locust.
    Канал собирается через build_gateway_locust_grpc_client (интерцептор метрик Locust).

    :param environment: окружение Locust для отправки событий request.
    :return: клиент DocumentsGatewayGRPCClient поверх канала с Locust-интерцептором.
    """
    return DocumentsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))
