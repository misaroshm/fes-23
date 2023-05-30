# Класи розробників
class Developer:
    def __init__(self, name):
        self.name = name

    def develop(self, task):
        print(f"{self.name} розробляє {task}.")

    def __str__(self):
        return self.name


class SoftwareArchitect:
    def __init__(self, name):
        self.name = name

    def architect(self, task):
        print(f"{self.name} проектує {task}.")

    def __str__(self):
        return self.name


class TeamLead:
    def __init__(self, name):
        self.name = name

    def manage_team(self):
        print(f"{self.name} керує командою.")

    def __str__(self):
        return self.name


class QualityControl:
    def __init__(self, name):
        self.name = name

    def test(self, task):
        print(f"{self.name} тестує {task}.")

    def __str__(self):
        return self.name


class BusinessAnalyst:
    def __init__(self, name):
        self.name = name

    def analyze(self, task):
        print(f"{self.name} аналізує {task}.")

    def __str__(self):
        return self.name


# Конвеєр розробки програмного забезпечення
class SoftwareDevelopmentPipeline:
    def __init__(self):
        self.developers = []
        self.architect = None
        self.team_lead = None
        self.qc = None
        self.ba = None

    def set_architect(self, architect):
        self.architect = architect

    def set_team_lead(self, team_lead):
        self.team_lead = team_lead

    def set_quality_control(self, qc):
        self.qc = qc

    def set_business_analyst(self, ba):
        self.ba = ba

    def add_developer(self, developer):
        self.developers.append(developer)

    def execute_project(self, project):
        print(f"Запуск проекту: {project}")
        self.ba.analyze(project)
        self.architect.architect(project)
        self.team_lead.manage_team()
        for developer in self.developers:
            developer.develop(project)
        self.qc.test(project)
        print("Проект завершено.")


# Замовник
class Client:
    def __init__(self):
        self.pipeline = None

    def create_pipeline(self):
        self.pipeline = SoftwareDevelopmentPipeline()

    def set_architect(self, architect):
        self.pipeline.set_architect(architect)

    def set_team_lead(self, team_lead):
        self.pipeline.set_team_lead(team_lead)

    def set_quality_control(self, qc):
        self.pipeline.set_quality_control(qc)

    def set_business_analyst(self, ba):
        self.pipeline.set_business_analyst(ba)

    def add_developer(self, developer):
        self.pipeline.add_developer(developer)

    def run_project(self, project):
        self.pipeline.execute_project(project)


def main():
    # Створюємо замовника та конвеєр
    client = Client()
    client.create_pipeline()

    # Запитуємо у замовника ім'я та завдання для проекту
    client_name = input("Введіть ваше ім'я: ")
    project_task = input("Введіть завдання для проекту: ")

    # Створюємо різних співробітників
    developer1 = Developer("Developer N1")
    developer2 = Developer("Developer N2")
    architect = SoftwareArchitect("Software Architector")
    team_lead = TeamLead("Team Lead")
    qc = QualityControl("Quality Analyst")
    ba = BusinessAnalyst("Business Analyst")

    # Налаштовуємо конвеєр
    client.set_architect(architect)
    client.set_team_lead(team_lead)
    client.set_quality_control(qc)
    client.set_business_analyst(ba)
    client.add_developer(developer1)
    client.add_developer(developer2)

    # Запускаємо проект
    print(f"\nЗамовник: {client_name}")
    print(f"Завдання для проекту: {project_task}\n")
    client.run_project(project_task)


if __name__ == "__main__":
    main()