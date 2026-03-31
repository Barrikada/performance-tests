import httpx

import time

# Создаём пользователя
create_user_payload = {
  "email": f"user{int(time.time() * 1000)}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}
create_user_response =  httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Создаем кредитный счёт для пользователя
open_credit_card_account_payload = {
    "userId": create_user_response_data['user']['id']
}
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()

# Совершаем операцию покупки
make_purchase_operation = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": open_credit_card_account_response_data['account']['cards'][0]['id'],
  "accountId": open_credit_card_account_response_data['account']['id'],
  "category": "Test"
}
make_purchase_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_operation)
make_purchase_operation_response_data = make_purchase_operation_response.json()

# Получаем чек по операции
operation_receipt = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/"
                              f"{make_purchase_operation_response_data['operation']['id']}")
operation_receipt_data = operation_receipt.json()
print(operation_receipt_data)