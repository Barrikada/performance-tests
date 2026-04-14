from seeds.scenario import SeedsScenario
from seeds.schema.plan import (
    SeedAccountsPlan,
    SeedOperationsPlan,
    SeedUsersPlan,
    SeedsPlan,
)


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который смотрит операции по кредитному счёту.
    Создаёт 300 пользователей, у каждого — один кредитный счёт с историей операций
    (покупки, пополнение, снятие наличных).
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга: 300 пользователей, по одному кредитному счёту;
        на счёте — 5 покупок, 1 пополнение, 1 снятие наличных.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),
                ),
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_get_operations"


if __name__ == "__main__":
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
