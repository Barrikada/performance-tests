from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedAccountsPlan, SeedUsersPlan, SeedsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который выпускает виртуальную карту.
    Создаёт 300 пользователей, каждому из которых открывается один дебетовый счёт.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга: сколько пользователей создать и какие счета открыть.
        Создаём 300 пользователей, у каждого — один дебетовый счёт.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                debit_card_accounts=SeedAccountsPlan(count=1),
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_issue_virtual_card"


if __name__ == "__main__":
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
