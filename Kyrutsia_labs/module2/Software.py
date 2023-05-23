from abc import ABC, abstractmethod


# Observer pattern
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Subject(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


# Software components
class SoftwareComponent:
    def __init__(self, name):
        self.name = name


class MobileApp(SoftwareComponent):
    def __init__(self, name, platform):
        super().__init__(name)
        self.platform = platform


class WebApp(SoftwareComponent):
    def __init__(self, name, backend, frontend):
        super().__init__(name)
        self.backend = backend
        self.frontend = frontend


class DatasetAPI(SoftwareComponent):
    def __init__(self, name):
        super().__init__(name)


class Containerization(SoftwareComponent):
    def __init__(self, name):
        super().__init__(name)


# Observer pattern implementation
class Developer(Subject):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def develop(self, software_component):
        print(f"{self.name} is developing {software_component.name}.")
        self.notify(f"{software_component.name} is developed.")
        if isinstance(software_component, DatasetAPI):
            numbers = list(range(1, 101))
            qa_result = self.qa_check(numbers)
            if qa_result:
                print(f"{self.name} received QA result: All numbers are even.")
            else:
                print(f"{self.name} received QA result: Some numbers are odd.")
                return numbers

    def qa_check(self, numbers):
        return all(num % 2 == 0 for num in numbers)


class QA(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received a message: {message}. Starting testing.")


class BusinessAnalyst(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received a message: {message}. Analyzing requirements.")


class TeamLead(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received a message: {message}. Reviewing code.")

