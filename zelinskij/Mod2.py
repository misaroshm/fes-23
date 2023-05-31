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


# Software class
class Software(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def develop(self):
        pass

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def deploy(self):
        pass


# Common software classes
class MobileApp(Software):
    def __init__(self, name: str):
        super().__init__(name)

    def develop(self):
        print(f"{self.name} is being developed for mobile platforms.")

    def test(self):
        print(f"{self.name} is being tested on mobile devices.")

    def deploy(self):
        print(f"{self.name} is being deployed to mobile app stores.")


class WebApp(Software):
    def __init__(self, name: str):
        super().__init__(name)

    def develop(self):
        print(f"{self.name} is being developed for web platforms.")

    def test(self):
        print(f"{self.name} is being tested on web browsers.")

    def deploy(self):
        print(f"{self.name} is being deployed to web servers.")


class JSBackend(Software):
    def __init__(self, name: str):
        super().__init__(name)

    def develop(self):
        print(f"{self.name} is being developed using JavaScript for backend.")

    def test(self):
        print(f"{self.name} is being tested for backend functionality.")

    def deploy(self):
        print(f"{self.name} is being deployed to backend servers.")


class PythonBackend(Software):
    def __init__(self, name: str):
        super().__init__(name)

    def develop(self):
        print(f"{self.name} is being developed using Python for backend.")

    def test(self):
        print(f"{self.name} is being tested for backend functionality.")

    def deploy(self):
        print(f"{self.name} is being deployed to backend servers.")


class JSFrontend(Software):
    def __init__(self, name: str):
        super().__init__(name)

    def develop(self):
        print(f"{self.name} is being developed using JavaScript for frontend.")

    def test(self):
        print(f"{self.name} is being tested for frontend functionality.")

    def deploy(self):
        print(f"{self.name} is being deployed to web servers.")


class DatabaseAPI(Software):
    def __init__(self, name: str):
        super().__init__(name)

    def develop(self):
        print(f"{self.name} is being developed as a database API.")

    def test(self):
        print(f"{self.name} is being tested for database connectivity.")

    def deploy(self):
        print(f"{self.name} is being deployed to database servers.")


class Containerization(Software):
    def __init__(self, name: str):
        super().__init__(name)

    def develop(self):
        print(f"{self.name} is being developed for containerization.")

    def test(self):
        print(f"{self.name} is being tested for containerization functionality.")

    def deploy(self):
        print(f"{self.name} is being deployed using containerization platforms.")


class Deployment(Software):
    def __init__(self, name: str):
        super().__init__(name)

    def develop(self):
        print(f"{self.name} is being developed for deployment.")

    def test(self):
        print(f"{self.name} is being tested for deployment readiness.")

    def deploy(self):
        print(f"{self.name} is being deployed to production servers.")


# main observer interface. used in pipeline, for example
class Observable(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# Testing Team Observer
class Observer:
    def __init__(self, name: str):
        self.name = name

    def update(self):
        print(f"QA {self.name} is testing the software.")


# software pipeline (composite pattern)
class SoftwarePipeline(Observable):
    def __init__(self):
        self.stages: list[Software] = []
        self.observers: list[Observer] = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def add_stage(self, stage: Software):
        self.stages.append(stage)

    def develop(self):
        print("Software development pipeline: Development phase")
        for stage in self.stages:
            stage.develop()

    def test(self):
        print("Software development pipeline: Testing phase")
        self.notify()

    def deploy(self):
        print("Software development pipeline: Deployment phase")
        for stage in self.stages:
            stage.deploy()


# 1. create team

# common devs
dev1, dev2 = Developer("Sam", 3, ["Python"]), Developer("Sean", 4, ["JS"])
# architect
arch = SoftwareArchitect("Lol", 6, ["Python", "JS"])
# team lead
leader = TeamLead("Euclid", 7, ["Python", "JS"], [dev1, dev2, arch])
# QA
qa = QA("Samantha", 2)
# business analyst
ba = BusinessAnalyst("Eva", 5)

team = [leader, dev1, dev2, arch, qa, ba]

# 2. create software pipeline
pipeline = SoftwarePipeline()

# 3. create software stages
mobile_app = MobileApp("My Mobile App")
web_app = WebApp("My Web App")
backend = PythonBackend("Backend Server")
frontend = JSFrontend("Frontend App")
database_api = DatabaseAPI("My Database API")
containerization = Containerization("My Containerization Platform")
deployment = Deployment("My Deployment Process")

# 4. add software stages to the pipeline
pipeline.add_stage(mobile_app)
pipeline.add_stage(web_app)
pipeline.add_stage(backend)
pipeline.add_stage(frontend)
pipeline.add_stage(database_api)
pipeline.add_stage(containerization)
pipeline.add_stage(deployment)

# 5. attach QA observer to the pipeline
pipeline.attach(qa)

# 6. develop software
pipeline.develop()

# 7. test software
pipeline.test()

# 8. deploy software
pipeline.deploy()

# 9. perform duties of the team members
for member in team:
    member.perform_duty()

deployment1.add_engineer(team_lead1)

app1.perform_engineering()
print("------------------------")
web_app1.perform_engineering()
print("------------------------")
database_api1.perform_engineering()
print("------------------------")
containerization1.perform_engineering()
print("------------------------")
deployment1.perform_engineering()
