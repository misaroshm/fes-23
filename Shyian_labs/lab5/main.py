from course import Course, Seminar
from personalInfo import PersonalInfo
from staff import Student, Professor


student_info_1 = PersonalInfo(id=1, _name='Julia_Simpson', address='Lviv', email='julia2003@gmail.com',
                              phone_number='067-97-606-32', position='Student', year=2004)
student_info_2 = PersonalInfo(id=1, _name='Cringe_Y', address='Kyiv', email='cringe2023@gmail.com',
                              phone_number='067-97-606-32', position='Student', year=2000)

student_1 = Student(personal_info=student_info_1, year=2019, lessons=4, days_visited=6)
student_2 = Student(personal_info=student_info_2,year=2022, lessons=2, days_visited=1)

student_1.__str__()
print()
student_1.ask_sick_leave()

course_java = Course(id=1, title='Java', student_id=student_info_1.id)
course_math = Course(id=1, title="Math", student_id=student_info_1.id)

print()
course_java.add_student(name=student_1.personal_info._name)
course_math.add_student(name=student_1.personal_info._name)
course_math.add_student(name=student_2.personal_info._name)
course_math.remove_student(name=student_1.personal_info._name)

print()
seminar = Seminar(id=2, title="Lab_1", deadline="13.08.2023", status=True)
seminar.add_comment(message="Good", title=seminar.title)

print()
professor_info = PersonalInfo(id=13, _name='Zlobin_GG', address='Lviv', phone_number='098-75-254-34',
                              email='zlobingg@gmail.com', position='Docent', year=1990)

professor = Professor(professor_info=professor_info, salary=13000, course="C/C++", days_visited=13)
professor.__str__()
print()
professor.ask_sick_leave()

