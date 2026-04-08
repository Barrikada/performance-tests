from __future__ import annotations

from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import OpenCreditCardAccountResponse
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import GetContractDocumentResponse
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import GetTariffDocumentResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse

from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.documents.client import build_documents_gateway_grpc_client
from clients.grpc.gateway.users.client import build_users_gateway_grpc_client


def main() -> None:
    """
    Выполняет цепочку вызовов gateway: пользователь → кредитный счёт → документы.

    Логирует ответы сервисов в stdout для проверки успешного прохождения сценария.
    """
    users_gateway_client = build_users_gateway_grpc_client()
    accounts_gateway_client = build_accounts_gateway_grpc_client()
    documents_gateway_client = build_documents_gateway_grpc_client()

    create_user_response: CreateUserResponse = users_gateway_client.create_user()
    print('Create user response:', create_user_response)

    open_credit_card_account_response: OpenCreditCardAccountResponse = (
        accounts_gateway_client.open_credit_card_account(user_id=create_user_response.user.id)
    )
    print('Open credit card account response:', open_credit_card_account_response)

    account_id: str = open_credit_card_account_response.account.id

    get_tariff_document_response: GetTariffDocumentResponse = documents_gateway_client.get_tariff_document(
        account_id=account_id
    )
    print('Get tariff document response:', get_tariff_document_response)

    get_contract_document_response: GetContractDocumentResponse = documents_gateway_client.get_contract_document(
        account_id=account_id
    )
    print('Get contract document response:', get_contract_document_response)


if __name__ == "__main__":
    main()
