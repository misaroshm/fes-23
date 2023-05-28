from abc import ABC, abstractmethod

# Спочатку імпортуємо ABC та abstractmethod з модуля abc.

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perform_duty(self):
        pass


# Створюємо базовий абстрактний клас Employee, який успадковують інші класи.
# Він містить абстрактний метод perform_duty, який потрібно реалізувати у підкласах.

class Developer(Employee):
    def __init__(self, name, skills):
        super().__init__(name)
        self.skills = skills

    def perform_duty(self):
        print(f"{self.name} is developing software.")


# Клас Developer успадковує Employee і реалізує метод perform_duty.
# У нього також є додатковий атрибут skills (навички розробника).

class SoftwareArchitect(Employee):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is designing software architecture.")


# Клас SoftwareArchitect успадковує Employee і реалізує метод perform_duty.

class TeamLead(Employee):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is leading the team.")


# Клас TeamLead успадковує Employee і реалізує метод perform_duty.

class QA(Employee):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is performing software testing.")


# Клас QA успадковує Employee і реалізує метод perform_duty.

class BusinessAnalyst(Employee):
    def __init__(self, name):
        super().__init__(name)

    def perform_duty(self):
        print(f"{self.name} is analyzing business requirements.")


# Клас BusinessAnalyst успадковує Employee і реалізує метод perform_duty.


class Software:
    def __init__(self, name):
        self.name = name
        self.engineers = []

    def add_engineer(self, engineer):
        self.engineers.append(engineer)

    def perform_engineering(self):
        print(f"Software {self.name} development pipeline:")
        for step in self.engineers:
            step.perform_duty()

# Клас Software представляє програмне забезпечення.



# Приклад взаємодії працівників та програмного забезпечення

developer1 = Developer("Person1", ["C", "C++"])
developer2 = Developer("Person2", ["JS", "Java"])
architect1 = SoftwareArchitect("Person3")
team_lead1 = TeamLead("Person4")
qa1 = QA("Person5")
business_analyst1 = BusinessAnalyst("Person6")

# Створюємо об'єкти різних класів, які представляють працівників.

app1 = Software("App")
app1.add_engineer(developer1)
app1.add_engineer(architect1)
app1.add_engineer(qa1)

# Створюємо об'єкт Software (програмне забезпечення) з назвою "App" та додаємо до нього різних інженерів.

web_app1 = Software("WebApp")
web_app1.add_engineer(developer2)
web_app1.add_engineer(architect1)
web_app1.add_engineer(qa1)

# Створюємо ще один об'єкт Software з назвою "WebApp" та додаємо до нього інших інженерів.

database_app1 = Software("DatabaseApp")
database_app1.add_engineer(developer1)
database_app1.add_engineer(developer2)
database_app1.add_engineer(architect1)
database_app1.add_engineer(qa1)

# Створюємо ще один об'єкт Software з назвою "DatabaseApp" та додаємо до нього інженерів.

containerization1 = Software("Containerization")
containerization1.add_engineer(developer1)
containerization1.add_engineer(architect1)
containerization1.add_engineer(team_lead1)

# Створюємо ще один об'єкт Software з назвою "Containerization" та додаємо до нього інженерів.

deployment1 = Software("Deployment")
deployment1.add_engineer(developer1)
deployment1.add_engineer(developer2)
deployment1.add_engineer(architect1)
deployment1.add_engineer(team_lead1)

# Створюємо ще один об'єкт Software з назвою "Deployment" та додаємо до нього інженерів.

app1.perform_engineering()
print("------------------------")
web_app1.perform_engineering()
print("------------------------")
database_app1.perform_engineering()
print("------------------------")
containerization1.perform_engineering()
print("------------------------")
deployment1.perform_engineering()
