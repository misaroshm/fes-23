import sqlite3

class Employee:
    def __init__(self, name, email, role):
        self.email = email
        self.name = name
        self.role = role

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nRole: {self.role}\n"


class Developer(Employee):
    def __init__(self, name, email, programming_languages):
        super().__init__(name, email, 'Developer')
        self.programming_languages = programming_languages

    def write_code(self):
        # Method to write code
        pass

    def __str__(self):
        return super().__str__() + f"Programming Languages: {', '.join(self.programming_languages)}\n"


class SoftwareArchitect(Employee):
    def __init__(self, name, email, experience):
        super().__init__(name, email, 'Software Architect')
        self.experience = experience

    def design_system(self):
        # Method to design the software system
        pass

    def __str__(self):
        return super().__str__() + f"Experience: {self.experience} years\n"


class TeamLead(Employee):
    def __init__(self, name, email, team_size):
        super().__init__(name, email, 'Team Lead')
        self.team_size = team_size

    def manage_team(self):
        # Method to manage the development team
        pass

    def __str__(self):
        return super().__str__() + f"Team Size: {self.team_size}\n"


class QA(Employee):
    def __init__(self, name, email, testing_frameworks):
        super().__init__(name, email, 'QA')
        self.testing_frameworks = testing_frameworks

    def perform_testing(self):
        # Method to perform software testing
        pass

    def __str__(self):
        return super().__str__() + f"Testing Frameworks: {', '.join(self.testing_frameworks)}\n"


class BusinessAnalyst(Employee):
    def __init__(self, name, email, domain_knowledge):
        super().__init__(name, email, 'Business Analyst')
        self.domain_knowledge = domain_knowledge

    def gather_requirements(self):
        # Method to gather project requirements
        pass

    def __str__(self):
        return super().__str__() + f"Domain Knowledge: {self.domain_knowledge}\n"




class MobileApp:
    def __init__(self, android, ios):
        self.android = android
        self.ios = ios

    def develop(self):
        # Method to develop the mobile app
        pass

    def __str__(self):
        return f"Android: {self.android}\niOS: {self.ios}\n"


class WebApp:
    def __init__(self, js_backend, python_backend, js_frontend):
        self.js_backend = js_backend
        self.python_backend = python_backend
        self.js_frontend = js_frontend

    def develop(self):
        # Method to develop the web app
        pass

    def __str__(self):
        return (
            f"JS Backend: {self.js_backend}\n"
            f"Python Backend: {self.python_backend}\n"
            f"JS Frontend: {self.js_frontend}\n"
        )

class Database:
    def __init__(self, name, database_api):
        self.name = name
        self.database_api = database_api

    def __str__(self):
        return f"Database Name: {self.name}\n{self.database_api}"


class DatabaseAPI:
    def __init__(self, api_name, database_type, database_file):
        self.api_name = api_name
        self.database_type = database_type
        self.database_file = database_file
        self.database = {}

    def create_api(self):
        # Method for creating the database API
        self.database = {}

    def __str__(self):
        return f"API Name: {self.api_name}\nDatabase Type: {self.database_type}\n"


class Containerization:
    def __init__(self):
        self.technology = None

    def containerize(self):
        # Method to containerize the software
        pass

    def __str__(self):
        return f"Technology: {self.technology}\n"


class Deployment:
    def __init__(self):
        self.environment = None

    def deploy(self):
        # Method
        pass

    def __str__(self):
        return f"Environment: {self.environment}\n"


class Software:
    def __init__(self):
        self.mobile_app = None
        self.web_app = None
        self.database = None
        self.containerization = None
        self.deployment = None

    def __str__(self):
        return (
            f"Mobile App: {self.mobile_app}\n"
            f"Web App: {self.web_app}\n"
            f"Database: {self.database}\n"
            f"Containerization: {self.containerization}\n"
            f"Deployment: {self.deployment}\n"
        )


# Create team members
developer1 = Developer('John Doe', 'john@example.com', ['Python', 'Java'])
architect1 = SoftwareArchitect('Jane Smith', 'jane@example.com', 8)
team_lead = TeamLead('Alice Johnson', 'alice@example.com', 5)
qa_engineer = QA('Bob Williams', 'bob@example.com', ['Selenium', 'JUnit'])
business_analyst = BusinessAnalyst('Emily Davis', 'emily@example.com', 'Finance')

# Create software instance
software = Software()

# Assign components to the software
software.mobile_app = MobileApp(android=True, ios=True)
software.web_app = WebApp(js_backend=True, python_backend=True, js_frontend=True)
software.database = Database("MyDatabase", DatabaseAPI("MyAPI", "MySQL", "database.db"))
software.containerization = Containerization()
software.deployment = Deployment()

# Perform actions using the team members and software components
developer1.write_code()
architect1.design_system()
team_lead.manage_team()
qa_engineer.perform_testing()
business_analyst.gather_requirements()

software.mobile_app.develop()
software.web_app.develop()

software.containerization.containerize()
software.deployment.deploy()


# Print the results
print("Team Members:")
print(developer1)
print(architect1)
print(team_lead)
print(qa_engineer)
print(business_analyst)

print("Software Components:")
print(software)

print("Database:")
print(software.database)

print("Containerization:")
print(software.containerization)

print("Deployment:")
print(software.deployment)