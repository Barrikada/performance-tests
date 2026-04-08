from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse

from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client
from clients.grpc.gateway.users.client import build_users_gateway_grpc_client


def main() -> None:
    """
    Создаёт пользователя, открывает дебетовый счёт и выполняет операцию пополнения.

    Печатает ответы сервисов в stdout.
    """
    users_gateway_client = build_users_gateway_grpc_client()
    accounts_gateway_client = build_accounts_gateway_grpc_client()
    operations_gateway_client = build_operations_gateway_grpc_client()

    create_user_response: CreateUserResponse = users_gateway_client.create_user()
    print('Create user response:', create_user_response)

    open_debit_card_account_response: OpenDebitCardAccountResponse = (
        accounts_gateway_client.open_debit_card_account(user_id=create_user_response.user.id)
    )
    print('Open debit card account response:', open_debit_card_account_response)

    account_id: str = open_debit_card_account_response.account.id
    card_id: str = open_debit_card_account_response.account.cards[0].id

    make_top_up_operation_response: MakeTopUpOperationResponse = operations_gateway_client.make_top_up_operation(
        card_id=card_id,
        account_id=account_id,
    )
    print('Make top up operation response:', make_top_up_operation_response)


if __name__ == '__main__':
    main()
