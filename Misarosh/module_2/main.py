class Observer:
    """
        Observer is a base class representing an observer in the Observer design pattern.
        It provides a common interface for all concrete observers.

        Attributes:
        - name: A string representing the name of the observer.

        Methods:
        - update(event): This method is called by the subject to notify the observer of an update.
                         It can be overridden by concrete observers to define specific behavior
                         when receiving an update.
    """
    def __init__(self, name):
        self.name = name

    def update(self, event):
        pass


class Developer(Observer):
    """
        A class representing a developer who works on the project.
        Inherits from the Observer class.

        Attributes:
            name (str): The name of the developer.
            skills (list): The skills possessed by the developer.

        Methods:
            update(event): Receives updates from the subject.
            work(): Performs work on the project.
        """
    def __init__(self, name, skills):
        super().__init__(name)
        self.skills = skills

    def update(self, event):
        print(f"{self.name} received update: {event}")

    def work(self):
        print(f"{self.name} is working on the project.")


class SoftwareArchitect(Observer):
    """
        A class representing a software architect.
        The software architect is responsible for designing the project and
        receiving updates about the project's progress.

        Attributes:
            name (str): The name of the software architect.
            experience (int): The number of years of experience of the software architect.

        Methods:
            update(event):
                Receives an update from the subject.
            design():
                Performs the design of the project.

        """
    def __init__(self, name, experience):
        super().__init__(name)
        self.experience = experience

    def update(self, event):
        print(f"{self.name} received update: {event}")

    def design(self):
        print(f"{self.name} is designing the project.")


class TeamLead(Observer):
    """
       A class representing a Team Lead, which is an observer in the project.

       Attributes:
           name (str): The name of the Team Lead.
           years_of_experience (int): The years of experience of the Team Lead.
    """
    def __init__(self, name, years_of_experience):
        super().__init__(name)
        self.years_of_experience = years_of_experience

    def update(self, event):
        print(f"{self.name} received update: {event}")

    def lead(self):
        print(f"{self.name} is leading the project team.")


class QA(Observer):
    """
       A class representing a QA specialist.

       Attributes:
           name (str): The name of the QA specialist.
           expertise (str): The area of expertise of the QA specialist.

       Methods:
           update(event):
               Receives an update from the subject and prints the received event.
           test():
               Performs testing for the project and prints a message indicating the QA specialist is testing.

       """
    def __init__(self, name, expertise):
        super().__init__(name)
        self.expertise = expertise

    def update(self, event):
        print(f"{self.name} received update: {event}")

    def test(self):
        print(f"{self.name} is testing the project.")


class BusinessAnalyst(Observer):
    """
        A class representing a Business Analyst.

        Attributes:
        - name (str): The name of the Business Analyst.
        - domain_knowledge (str): The domain knowledge of the Business Analyst.

        Methods:
        - update(event): Update method called when the Business Analyst receives an update from the subject.
        - analyze(): Perform the task of analyzing the project requirements.
        """
    def __init__(self, name, domain_knowledge):
        super().__init__(name)
        self.domain_knowledge = domain_knowledge

    def update(self, event):
        print(f"{self.name} received update: {event}")

    def analyze(self):
        print(f"{self.name} is analyzing the project requirements.")


class Subject:
    """
        A class representing the subject being observed.

        Attributes:
            observers (list): A list of observers attached to the subject.

        Methods:
            __init__(): Initializes a new instance of the Subject class.
            attach(observer): Attaches an observer to the subject.
            detach(observer): Detaches an observer from the subject.
            notify(event): Notifies all attached observers with the given event.
        """
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)


# Create instances of the classes (team)
developer1 = Developer("Lola Smith", ["Python", "Java"])
developer2 = Developer("John Peterson", ["JavaScript", "Python", "C/C++"])
software_architect = SoftwareArchitect("Julia R.", 10)
team_lead = TeamLead("Zlobin GG", 5)
qa = QA("Susan B.", "UI/UX")
business_analyst = BusinessAnalyst("David T.", "Finance")

# Create the subject (project)
project = Subject()

# Attach the observers to the subject
project.attach(developer1)
project.attach(developer2)
project.attach(software_architect)
project.attach(team_lead)
project.attach(qa)
project.attach(business_analyst)

# Start working on the project
project.notify("Project started")

print()

# Develop the software
project.notify("Software development in progress")

print()

# Detach observers if necessary
project.detach(developer2)

# Continue with the project
project.notify("Software development completed")
print()
# Output the current status
project.notify("Project finished")
