from abc import ABC, abstractmethod

class TeamMember(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perform_duty(self):
        pass

class Developer(TeamMember):
    def __init__(self, name, skills):
        super().__init__(name)
        self.skills = skills

    def perform_duty(self):
        print(f"Developer {self.name} is developing software.")

class SoftwareArchitect(TeamMember):
    def perform_duty(self):
        print(f"Software Architect {self.name} is designing software architecture.")

class TeamLead(TeamMember):
    def perform_duty(self):
        print(f"Team Lead {self.name} is managing the team.")

class QA(TeamMember):
    def perform_duty(self):
        print(f"QA {self.name} is testing the software.")

class BusinessAnalyst(TeamMember):
    def perform_duty(self):
        print(f"Business Analyst {self.name} is analyzing the requirements.")

class Software(ABC):
    @abstractmethod
    def develop(self):
        pass

class MobileApp(Software):
    def develop(self):
        print("Developing Mobile App.")

class WebApp(Software):
    def develop(self):
        print("Developing Web App.")

class DatabaseAPI(Software):
    def develop(self):
        print("Developing Database API.")

class Containerization(Software):
    def develop(self):
        print("Performing Containerization.")

class Deployment(Software):
    def develop(self):
        print("Performing Deployment.")

class Project:
    def __init__(self):
        self.team_members = []
        self.software_components = []

    def add_team_member(self, team_member):
        self.team_members.append(team_member)

    def add_software_component(self, software_component):
        self.software_components.append(software_component)

    def execute_pipeline(self):
        for member in self.team_members:
            member.perform_duty()

        for component in self.software_components:
            component.develop()

def main():
    project = Project()

    developer1 = Developer("Mari", ["Python", "Java"])
    developer2 = Developer("Maks", ["JavaScript", "C++"])
    architect = SoftwareArchitect("Kate")
    team_lead = TeamLead("Marina")
    qa = QA("Valentyn")
    analyst = BusinessAnalyst("Arthur")

    project.add_team_member(developer1)
    project.add_team_member(developer2)
    project.add_team_member(architect)
    project.add_team_member(team_lead)
    project.add_team_member(qa)
    project.add_team_member(analyst)

    mobile_app = MobileApp()
    web_app = WebApp()
    database_api = DatabaseAPI()
    containerization = Containerization()
    deployment = Deployment()

    project.add_software_component(mobile_app)
    project.add_software_component(web_app)
    project.add_software_component(database_api)
    project.add_software_component(containerization)
    project.add_software_component(deployment)

    project.execute_pipeline()

if __name__ == "__main__":
    main()
