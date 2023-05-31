# all employees classes in this file

from abc import ABC, abstractmethod


# abstract member
class TeamMember(ABC):
    def __init__(self, name: str, exp_years: int):
        self.name = name
        self.exp_years = exp_years

    @abstractmethod
    def perform_duty(self) -> None:
        pass


# certain developer defined by self.specs (skills)
class Developer(TeamMember):
    def __init__(self, name: str, exp_years: int, specs: list[str]):
        super().__init__(name, exp_years)
        self.specs = specs

    def perform_duty(self) -> None:
        print(f"Developer {self.name} is developing software...")


class SoftwareArchitect(Developer):
    def __init__(self, name: str, exp_years: int, specs: list[str]):
        super().__init__(name, exp_years, specs)

    def perform_duty(self) -> None:
        print(f"Software Architect {self.name} is designing software architecture...")


class TeamLead(Developer):
    def __init__(self, name: str, exp_years: int, skills: list[str], team: list[Developer]):
        super().__init__(name, exp_years, skills)
        self.team = team

    def perform_duty(self) -> None:
        print(f"TeamLead {self.name} is managing the team . . .")


class QA(TeamMember):
    def __init__(self, name: str, exp_years: int):
        super().__init__(name, exp_years)

    def perform_duty(self) -> None:
        print(f"Quality Assurance  {self.name} is testing software . . .")


class BusinessAnalyst(TeamMember):
    def __init__(self, name: str, exp_years: int):
        super().__init__(name, exp_years)

    def perform_duty(self) -> None:
        print(f"Business Analyst {self.name} is gathering requirements . . .")


