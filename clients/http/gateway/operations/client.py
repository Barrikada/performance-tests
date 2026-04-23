from httpx import QueryParams, Response
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.operations.schema import (
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationsSummaryResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
    OperationStatus,
)
from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from tools.routes import APIRoutes


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения информации об операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(
            f"{APIRoutes.OPERATIONS}/{operation_id}",
            extensions=HTTPClientExtensions(route=f"{APIRoutes.OPERATIONS}/{{operation_id}}"),
        )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения чека по операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными чека.
        """
        return self.get(
            f"{APIRoutes.OPERATIONS}/operation-receipt/{operation_id}",
            extensions=HTTPClientExtensions(
                route=f"{APIRoutes.OPERATIONS}/operation-receipt/{{operation_id}}"
            ),
        )

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос для получения списка операций по счёту.

        :param query: Pydantic-модель с параметром accountId.
        :return: Объект httpx.Response со списком операций.
        """
        return self.get(
            APIRoutes.OPERATIONS,
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route=APIRoutes.OPERATIONS),
        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос для получения сводки по операциям по счёту.

        :param query: Pydantic-модель с параметром accountId.
        :return: Объект httpx.Response со статистикой по операциям.
        """
        return self.get(
            f"{APIRoutes.OPERATIONS}/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route=f"{APIRoutes.OPERATIONS}/operations-summary"),
        )

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Тело запроса с данными для создания операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            f"{APIRoutes.OPERATIONS}/make-fee-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Тело запроса с данными для создания операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            f"{APIRoutes.OPERATIONS}/make-top-up-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Тело запроса с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            f"{APIRoutes.OPERATIONS}/make-cashback-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Тело запроса с данными для создания операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            f"{APIRoutes.OPERATIONS}/make-transfer-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Тело запроса с данными для создания операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            f"{APIRoutes.OPERATIONS}/make-purchase-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счёту.

        :param request: Тело запроса с данными для создания операции оплаты по счёту.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            f"{APIRoutes.OPERATIONS}/make-bill-payment-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequestSchema
    ) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Тело запроса с данными для создания операции снятия наличных денег.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            f"{APIRoutes.OPERATIONS}/make-cash-withdrawal-operation",
            json=request.model_dump(by_alias=True),
        )

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operations(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        return self.make_top_up_operations(card_id, account_id)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(
        self, card_id: str, account_id: str
    ) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())


def build_operations_gateway_locust_http_client(environment: Environment) -> OperationsGatewayHTTPClient:
    """
    Создаёт OperationsGatewayHTTPClient для нагрузочных тестов с Locust.

    HTTP-клиент собирает метрики через event hooks (см. build_gateway_locust_http_client).

    :param environment: окружение Locust для отправки событий request.
    :return: экземпляр OperationsGatewayHTTPClient с подключённым locust-совместимым httpx.Client.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))

