from abc import ABC, abstractmethod


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

