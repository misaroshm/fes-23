class Course:
    """
    Initialize a Course instance.

    Args:
        - id (int): The unique identifier of the course.
        - title (str): The title of the course.
        - student_id (list): List of student IDs enrolled in the course.
    """
    def __init__(self, id: int, title: str, student_id: []):
        self.title = title
        self.id = id
        self.student_id = student_id
        self.students_added = []

    def add_student(self, name: str):
        """
        Add a student to the course.

        Args:
            - name (str): The name of the student to add.
        """
        self.students_added.append(name)
        print(f"Student {name} is added to {self.title} course!")

    def remove_student(self, name: str):
        """
        Remove a student from the course.

        Args:
            - name (str): The name of the student to remove.
        """
        self.students_added.remove(name)
        print(f"Student {name} is removed from {self.title} course!")


class Seminar:
    """
    Initialize a Seminar instance.

    Args:
        - id (int): The unique identifier of the seminar.
        - title (str): The title of the seminar.
        - deadline (str): The deadline for the seminar.
        - status (bool): The status of the seminar (e.g., completed or ongoing).
    """
    def __init__(self, id: int, title: str, deadline: str, status: bool):
        self.id = id
        self.title = title
        self.deadline = deadline
        self.status = status

    def add_comment(self, message: str):
        """
        Add a comment to the seminar.

        Args:
            - message (str): The comment message.
        """
        print(f"Comment to {self.title}: {message}")
