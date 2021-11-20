class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturers_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'
    pass

    def average_grade(self):
        numbers = list()
        for i in self.grades.values():
            numbers += i
        av = float(sum(numbers)/len(numbers))
        return av
    pass

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
        return self.average_grade() < other.average_grade()

    def __str__(self):
        student_dict = {'Имя:': self.name, 'Фамилия:': self.surname,
                        'Средняя оценка за домашние задания:': self.average_grade(),
                        'Курсы в процессе изучения:': ', '.join(self.courses_in_progress),
                        'Завершенные курсы:': ', '.join(self.finished_courses)}
        for k,v in student_dict.items(): print(k,v)
        return

student_1 = Student('Vasya', 'Pupkin', 'male')
student_1.courses_in_progress = ['Python', 'Git']
student_1.grades = {'Python': [], 'Git': []}
student_1.finished_courses = ['Введение в программирование']

student_2 = Student('Petya', 'Ivanov', 'male')
student_2.courses_in_progress = ['Git']
student_2.grades = {'Git': []}

students_list = [student_1, student_2]

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_from_students = {'Python': [], 'Git': []}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        pass

    def __str__(self):
        reviewer_dict = {'Имя:': self.name, 'Фамилия:': self.surname}
        for k,v in reviewer_dict.items(): print(k,v)
        return

reviewer_1 = Reviewer('Vitaliy', 'Kholodov')
reviewer_1.courses_attached = ['Python']

reviewer_2 = Reviewer('Anna', 'Morozova')
reviewer_2.courses_attached = ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 9)
print(student_1.grades)

reviewer_2.rate_hw(student_2, 'Git', 8)
print(student_2.grades)

print(student_1.average_grade())
print(student_2.average_grade())

class Lecturer(Mentor):
    def l_average_grade(self):
        numbers = list()
        for i in self.grades_from_students.values():
            numbers += i
        l_av = float(sum(numbers)/len(numbers))
        return l_av
    pass

    def __str__(self):
        lecturer_dict = {'Имя:': self.name, 'Фамилия:': self.surname, 'Средняя оценка за лекции:': self.l_average_grade()}
        for k, v in lecturer_dict.items(): print(k, v)
        return

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
        return self.l_average_grade() < other.l_average_grade()

lecturer_1 = Lecturer('Victor', 'Dobrov')
lecturer_1.courses_attached = ['Python']
lecturer_1.grades_from_students = {'Python': []}

lecturer_2 = Lecturer('Aleksey', 'Zubov')
lecturer_2.courses_attached = ['Python', 'Git']
lecturer_2.grades_from_students = {'Python': [], 'Git': []}

lecturers_list = [lecturer_1, lecturer_2]

student_1.lecturers_rate(lecturer_1, 'Python', 10)
student_1.lecturers_rate(lecturer_2, 'Python', 8)
print(lecturer_1.grades_from_students)

student_2.lecturers_rate(lecturer_2, 'Git', 9)
print(lecturer_2.grades_from_students)

print(lecturer_1.l_average_grade())
print(lecturer_2.l_average_grade())

print(student_1)

print(reviewer_1)

print(lecturer_1)

print(student_1 > student_2)
print(lecturer_1 < lecturer_2)


def average_students_rate(students_list, course):
    list_1 = []
    for i in students_list:
        if course in i.courses_in_progress:
            list_1 += i.grades[course]
            av_st = float(sum(list_1)/ len(students_list))
        return av_st

def average_lecturers_rate(lecturers_list, course):
    list_2 = []
    for i in lecturers_list:
        if course in i.courses_attached:
            list_2 += i.grades_from_students[course]
            print(i.grades_from_students[course])
            av_lec = float(sum(list_2)/ len(lecturers_list))
    return av_lec

print(average_students_rate(students_list, 'Python'))
print(average_lecturers_rate(lecturers_list, 'Python'))
