from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    PURCHASE = "PURCHASE"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    FAILED = "FAILED"


class OperationSchema(BaseModel):
    """
    Структура операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str | None = None
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Структура чека операции.
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Структура сводки по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека операции.
    """
    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа получения сводки по операциям.
    """
    summary: OperationsSummarySchema


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения сводки по операциям по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбэка.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции перевода.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции покупки.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=fake.category)


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции оплаты по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции снятия наличных денег.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции комиссии.
    """
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции пополнения.
    """
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции перевода.
    """
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции оплаты по счёту.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа создания операции снятия наличных.
    """
    operation: OperationSchema
