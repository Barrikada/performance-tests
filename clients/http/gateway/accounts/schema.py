from pydantic import BaseModel

from clients.http.gateway.cards.schema import CardSchema


class AccountSchema(BaseModel):
    """
    Описание структуры счёта в ответе API.
    """
    id: str
    type: str
    cards: list[CardSchema]
    status: str
    balance: float


class OpenAccountResponseSchema(BaseModel):
    """
    Ответ эндпоинтов открытия счёта (дебет/кредит и т.д.).
    """
    account: AccountSchema
