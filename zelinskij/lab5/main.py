from personalInfo import PersonalInfo
from staff import Student, Professor
from course import Course
from seminar import Seminar

# Creating personal info for students
student_info_1 = PersonalInfo(id=1, _name='Julia_Simpson', address='Lviv', email='julia2003@gmail.com',
                              phone_number='067-97-606-32', position='Student', year=2004)
student_info_2 = PersonalInfo(id=2, _name='Cringe_Y', address='Kyiv', email='cringe2023@gmail.com',
                              phone_number='067-97-606-32', position='Student', year=2000)

# Creating student instances
student_1 = Student(personal_info=student_info_1, year=2019, lessons=4, days_visited=6)
student_2 = Student(personal_info=student_info_2, year=2022, lessons=2, days_visited=1)

# Printing student details
print(student_1)
print()

# Asking for sick leave
student_1.ask_sick_leave()

# Creating courses
course_java = Course(id=1, title='Java', student_id=[student_info_1.id])
course_math = Course(id=2, title="Math", student_id=[student_info_1.id])

# Adding and removing students from courses
course_java.add_student(name=student_info_1._name)
course_math.add_student(name=student_info_1._name)
course_math.add_student(name=student_info_2._name)
course_math.remove_student(name=student_info_1._name)

# Creating a seminar
seminar = Seminar(id=2, title="Lab_1", deadline="13.08.2023", status=True)
seminar.add_comment(message="Good")

# Creating personal info for a professor
professor_info = PersonalInfo(id=13, _name='Zlobin_GG', address='Lviv', phone_number='098-75-254-34',
                              email='zlobingg@gmail.com', position='Docent', year=1990)

# Creating a professor instance
professor = Professor(professor_info=professor_info, salary=13000, course=course_java, days_visited=13)

# Printing professor details
print(professor)
print()

# Asking for sick leave
professor.ask_sick_leave()
