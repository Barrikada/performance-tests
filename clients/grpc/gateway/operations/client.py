from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse,
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse,
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse,
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse,
)
from contracts.services.operations.operation_pb2 import OperationStatus

from tools.fakers import fake


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.

    Низкоуровневые методы вызывают соответствующие RPC напрямую; высокоуровневые
    формируют запросы (для операций создания — с фейковыми суммой, категорией и статусом).
    """

    def __init__(self, channel: Channel) -> None:
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)

        self.stub: OperationsGatewayServiceStub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов GetOperation: данные одной операции по идентификатору.

        :param request: Запрос GetOperationRequest (поле id — идентификатор операции).
        :return: Ответ GetOperationResponse с сообщением Operation.
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов GetOperationReceipt: чек по идентификатору операции.

        :param request: Запрос GetOperationReceiptRequest с operation_id.
        :return: Ответ GetOperationReceiptResponse с Receipt.
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов GetOperations: список операций по счёту.

        :param request: Запрос GetOperationsRequest с account_id.
        :return: Ответ GetOperationsResponse со списком Operation.
        """
        return self.stub.GetOperations(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов GetOperationsSummary: агрегированная статистика по счёту.

        :param request: Запрос GetOperationsSummaryRequest с account_id.
        :return: Ответ GetOperationsSummaryResponse с OperationsSummary.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов MakeFeeOperation: создание операции комиссии.

        :param request: Запрос MakeFeeOperationRequest.
        :return: Ответ MakeFeeOperationResponse с созданной Operation.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов MakeTopUpOperation: создание операции пополнения.

        :param request: Запрос MakeTopUpOperationRequest.
        :return: Ответ MakeTopUpOperationResponse с созданной Operation.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов MakeCashbackOperation: создание операции кэшбэка.

        :param request: Запрос MakeCashbackOperationRequest.
        :return: Ответ MakeCashbackOperationResponse с созданной Operation.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов MakeTransferOperation: создание операции перевода.

        :param request: Запрос MakeTransferOperationRequest.
        :return: Ответ MakeTransferOperationResponse с созданной Operation.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов MakePurchaseOperation: создание операции покупки.

        :param request: Запрос MakePurchaseOperationRequest.
        :return: Ответ MakePurchaseOperationResponse с созданной Operation.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequest
    ) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов MakeBillPaymentOperation: создание операции оплаты счёта.

        :param request: Запрос MakeBillPaymentOperationRequest.
        :return: Ответ MakeBillPaymentOperationResponse с созданной Operation.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequest
    ) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов MakeCashWithdrawalOperation: создание операции снятия наличных.

        :param request: Запрос MakeCashWithdrawalOperationRequest.
        :return: Ответ MakeCashWithdrawalOperationResponse с созданной Operation.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Возвращает операцию по идентификатору.

        :param operation_id: Идентификатор операции (маппится в поле id запроса protobuf).
        :return: Ответ GetOperationResponse.
        """
        request: GetOperationRequest = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Возвращает чек по идентификатору операции.

        :param operation_id: Идентификатор операции.
        :return: Ответ GetOperationReceiptResponse.
        """
        request: GetOperationReceiptRequest = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Возвращает список операций по счёту.

        :param account_id: Идентификатор счёта.
        :return: Ответ GetOperationsResponse.
        """
        request: GetOperationsRequest = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Возвращает сводку по операциям для счёта.

        :param account_id: Идентификатор счёта.
        :return: Ответ GetOperationsSummaryResponse.
        """
        request: GetOperationsSummaryRequest = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """
        Создаёт операцию комиссии с фейковыми суммой и статусом.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ MakeFeeOperationResponse.
        """
        request: MakeFeeOperationRequest = MakeFeeOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """
        Создаёт операцию пополнения с фейковыми суммой и статусом.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ MakeTopUpOperationResponse.
        """
        request: MakeTopUpOperationRequest = MakeTopUpOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        """
        Создаёт операцию кэшбэка с фейковыми суммой и статусом.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ MakeCashbackOperationResponse.
        """
        request: MakeCashbackOperationRequest = MakeCashbackOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        """
        Создаёт операцию перевода с фейковыми суммой и статусом.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ MakeTransferOperationResponse.
        """
        request: MakeTransferOperationRequest = MakeTransferOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        """
        Создаёт операцию покупки с фейковыми суммой, категорией и статусом.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ MakePurchaseOperationResponse.
        """
        request: MakePurchaseOperationRequest = MakePurchaseOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            category=fake.category(),
            account_id=account_id,
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        """
        Создаёт операцию оплаты по счёту с фейковыми суммой и статусом.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ MakeBillPaymentOperationResponse.
        """
        request: MakeBillPaymentOperationRequest = MakeBillPaymentOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        """
        Создаёт операцию снятия наличных с фейковыми суммой и статусом.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счёта.
        :return: Ответ MakeCashWithdrawalOperationResponse.
        """
        request: MakeCashWithdrawalOperationRequest = MakeCashWithdrawalOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())


def build_operations_gateway_locust_grpc_client(environment: Environment) -> OperationsGatewayGRPCClient:
    """
    Создаёт OperationsGatewayGRPCClient для нагрузочного тестирования в Locust.
    Канал собирается через build_gateway_locust_grpc_client (интерцептор метрик Locust).

    :param environment: окружение Locust для отправки событий request.
    :return: клиент OperationsGatewayGRPCClient поверх канала с Locust-интерцептором.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))
