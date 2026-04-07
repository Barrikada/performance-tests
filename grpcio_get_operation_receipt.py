import grpc

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse,
)
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse,
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse,
)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.operations.operation_pb2 import OperationStatus

from tools.fakers import fake

GATEWAY_TARGET: str = "localhost:9003"


def main() -> None:
    channel: grpc.Channel = grpc.insecure_channel(GATEWAY_TARGET)

    users_gateway: UsersGatewayServiceStub = UsersGatewayServiceStub(channel)
    accounts_gateway: AccountsGatewayServiceStub = AccountsGatewayServiceStub(channel)
    operations_gateway: OperationsGatewayServiceStub = OperationsGatewayServiceStub(channel)

    create_user_request: CreateUserRequest = CreateUserRequest(
        email=fake.email(),
        last_name=fake.last_name(),
        first_name=fake.first_name(),
        middle_name=fake.middle_name(),
        phone_number=fake.phone_number(),
    )
    create_user_response: CreateUserResponse = users_gateway.CreateUser(create_user_request)
    print("Create user response:", create_user_response)

    open_debit_request: OpenDebitCardAccountRequest = OpenDebitCardAccountRequest(
        user_id=create_user_response.user.id,
    )
    open_debit_response: OpenDebitCardAccountResponse = accounts_gateway.OpenDebitCardAccount(
        open_debit_request
    )
    print("Open debit card account response:", open_debit_response)

    make_top_up_request: MakeTopUpOperationRequest = MakeTopUpOperationRequest(
        status=OperationStatus.OPERATION_STATUS_COMPLETED,
        amount=fake.amount(),
        card_id=open_debit_response.account.cards[0].id,
        account_id=open_debit_response.account.id,
    )
    make_top_up_response: MakeTopUpOperationResponse = operations_gateway.MakeTopUpOperation(
        make_top_up_request
    )
    print("Make top up operation response:", make_top_up_response)

    get_receipt_request: GetOperationReceiptRequest = GetOperationReceiptRequest(
        operation_id=make_top_up_response.operation.id,
    )
    get_receipt_response: GetOperationReceiptResponse = operations_gateway.GetOperationReceipt(
        get_receipt_request
    )
    print("Get operation receipt response:", get_receipt_response)


if __name__ == "__main__":
    main()
