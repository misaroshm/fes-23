from abc import ABC, abstractmethod

from course import Course
from personalInfo import PersonalInfo


class Staff(ABC):
    """Abstract base class representing a staff member."""
    def __init__(self, personal_info: PersonalInfo):
        self._personal_info = personal_info

    @property
    def personal_info(self) -> PersonalInfo:
        """
        Get the personal information of the staff member.

        Returns:
            PersonalInfo: PersonalInfo object containing personal information.
        """
        return self._personal_info

    @personal_info.setter
    def personal_info(self, _personal_info: PersonalInfo):
        """
        Set the personal information of the staff member.

        Args:
            _personal_info: PersonalInfo object containing personal information.

        Raises:
            AttributeError: If the provided personal_info is not an instance of PersonalInfo.
        """
        if isinstance(_personal_info, PersonalInfo):
            self._personal_info = PersonalInfo
        else:
            raise AttributeError(f"Personal info must be an instance of PersonalInfo")

    @abstractmethod
    def ask_sick_leave(self) -> bool:
        """
        Ask for sick leave.

        Returns:
            bool: True if the sick leave is approved, False otherwise.
        """
        pass




class Student(Staff):
    """Class representing a student staff member."""
    def __init__(self, personal_info: PersonalInfo, year: int, lessons: int, days_visited: int) -> None:
        super().__init__(personal_info=personal_info)
        self.year = year
        self.lessons = lessons
        self.days_visited = days_visited

    def ask_sick_leave(self) -> str:
        """
        Ask for sick leave.

        Returns:
            bool: True if the sick leave is approved, False otherwise.

        Raises:
            ValueError: If the student has visited less than 5 days.
        """
        if self.days_visited >= 5:
            print("You can take sick leave")
        else:
            return ValueError("You should visit at least 5 days!")

    def __str__(self):
        return print(f"Name: {self._personal_info._name} \n"
                     f"Address: {self._personal_info.address} \n"
                     f"Phone number: {self._personal_info.phone_number} \n"
                     f"Email: {self._personal_info.email} \n"
                     f"Position: {self._personal_info.position} \n"
                     f"Employed year: {self.year}")

class Professor(Staff):
    """Class representing a professor staff member."""
    def __init__(self, professor_info: PersonalInfo, salary: float, course: Course, days_visited: int):
        super().__init__(personal_info=professor_info)
        self.professor_info = professor_info
        self.salary = salary
        self.course = course
        self.days_visited = days_visited

    @property
    def course(self):
        """
        Get the course taught by the professor.

        Returns:
            Course: Course object representing the course.
                """
        return self._course

    @course.setter
    def course(self, course: Course):
        """
        Set the course taught by the professor.

        Args:
            course: Course object representing the course.

        Raises:
            AttributeError: If the provided course is not an instance of Course.
        """
        self._course = course

    def ask_sick_leave(self):
        """
        Ask for sick leave.

        Returns:
            bool: True if the sick leave is approved, False otherwise.

        Raises:
            ValueError: If the professor has visited less than 10 days.
        """
        if self.days_visited >= 10:
            print("You can take sick leave")
        else:
            raise ValueError("You should visit at least 10 days!")

    def __str__(self):
        return print(f"Name: {self.professor_info.name}\n"
               f"Address: {self.professor_info.address}\n"
               f"Phone number: {self.professor_info.phone_number}\n"
               f"Email: {self.professor_info.email}\n" 
               f"Position: {self.professor_info.position}\n"
               f"Employed year: {self.professor_info.year}")


class PostgraduateStudent(Staff):
    """Class representing a postgraduate student staff member."""
    def __init__(self, personal_info: PersonalInfo, salary: float, lessons: int, days_visited: int) -> None:
        super().__init__(personal_info=personal_info)
        self.salary = salary
        self.lessons = lessons
        self.days_visited = days_visited

    def ask_sick_leave(self):
        """
        Ask for sick leave.

        Returns:
            bool: True if the sick leave is approved, False otherwise.
        Raises:
            ValueError: If the postgraduate student has visited less than 10 days.
       """
        if self.days_visited >= 10:
            return True
        else:
            return ValueError("You should visit at least 10 days!")


    def __str__(self):
        return print(f"Name: {self._personal_info._name} \n"
                     f"Address: {self._personal_info.address} \n"
                     f"Phone number: {self._personal_info.phone_number} \n"
                     f"Email: {self._personal_info.email} \n"
                     f"Position: {self._personal_info.position} \n"
                     f"Employed year: {self._personal_info.year} \n"
                     f"Salary: {self.salary}")
