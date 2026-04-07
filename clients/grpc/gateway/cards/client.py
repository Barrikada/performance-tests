from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardRequest,
    IssuePhysicalCardResponse,
)
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
    IssueVirtualCardRequest,
    IssueVirtualCardResponse,
)


class CardsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с CardsGatewayService в составе grpc-gateway.
    Оборачивает выпуск виртуальной и физической карты: низкоуровневые *_api и удобные обёртки.
    """

    def __init__(self, channel: Channel) -> None:
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: Канал до grpc-gateway (тот же, что и для остальных gateway-сервисов).
        """
        super().__init__(channel)
        self.stub: CardsGatewayServiceStub = CardsGatewayServiceStub(channel)

    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> IssueVirtualCardResponse:
        """
        Прямой вызов RPC CardsGatewayService.IssueVirtualCard.

        :param request: Сообщение IssueVirtualCardRequest.
        :return: Ответ сервиса IssueVirtualCardResponse.
        """
        return self.stub.IssueVirtualCard(request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        """
        Прямой вызов RPC CardsGatewayService.IssuePhysicalCard.

        :param request: Сообщение IssuePhysicalCardRequest.
        :return: Ответ сервиса IssuePhysicalCardResponse.
        """
        return self.stub.IssuePhysicalCard(request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponse:
        """
        Выпуск виртуальной карты по идентификаторам пользователя и счёта.

        :param user_id: Идентификатор пользователя.
        :param account_id: Идентификатор счёта.
        :return: Ответ с данными выпущенной карты.
        """
        request: IssueVirtualCardRequest = IssueVirtualCardRequest(
            user_id=user_id,
            account_id=account_id,
        )
        return self.issue_virtual_card_api(request)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        """
        Выпуск физической карты по идентификаторам пользователя и счёта.

        :param user_id: Идентификатор пользователя.
        :param account_id: Идентификатор счёта.
        :return: Ответ с данными выпущенной карты.
        """
        request: IssuePhysicalCardRequest = IssuePhysicalCardRequest(
            user_id=user_id,
            account_id=account_id,
        )
        return self.issue_physical_card_api(request)


def build_cards_gateway_grpc_client() -> CardsGatewayGRPCClient:
    """
    Собирает CardsGatewayGRPCClient с каналом до grpc-gateway.

    :return: Настроенный экземпляр CardsGatewayGRPCClient.
    """
    return CardsGatewayGRPCClient(channel=build_gateway_grpc_client())
