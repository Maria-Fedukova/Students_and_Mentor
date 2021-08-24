# Создаем класс студентов
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student_list = []

    # Метод, добавляющий курс в список законченных курсов
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

# Метод выставления оценок лекторам
    def grade_for_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        if not self.grades:
            print('Нет оценки!')
        else:
            grade = []
            for i in self.grades.values():
                grade += i
            return round((sum(grade) / len(grade)), 1)


# Перегрузка метода __str__
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average()}\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res


# Создаем родительский класс преподавателей
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Метод, закрепляющий курс за преподавателем
    def add_courses(self, course_name):
        self.courses_attached.append(course_name)


# Класс лекторов:
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def average_grades(self):
        if not self.grades:
            print('Нет оценки!')
        else:
            grade = []
            for i in self.grades.values():
                grade += i
            return round((sum(grade) / len(grade)), 1)
        if not self.grades:
            print('Нет оценки!')
        else:
            grade = []
            for i in self.grades.values():
                grade += i
            return round((sum(grade) / len(grade)), 1)

# Перегрузка метода __str__
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}'
        return res


# Класс экспертов, проверяющих домашнее задание:
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

# Метод выставления оценок студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Перегрузка метода __str__
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


# Создание экземпляров классов
some_reviewer = Reviewer('Some1', 'Buddy1')

some_lecturer = Lecturer('Some2', 'Buddy2')
some_lecturer.add_courses('Python')
some_lecturer.add_courses('Git')

some_student = Student('Ruoy1', 'Eman1', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

best_student = Student('best', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)

cool_mentor.rate_hw(some_student, 'Python', 9)
cool_mentor.rate_hw(some_student, 'Git', 9)
cool_mentor.rate_hw(some_student, 'Python', 9)
cool_mentor.rate_hw(some_student, 'Git', 9)

best_lector = Lecturer('Best', 'Buddy')
best_lector.courses_attached += ['Python']
best_lector.courses_attached += ['Git']

cool_student = Student('Ruoy', 'Eman', 'your_gender')
cool_student.add_courses('Python')
cool_student.add_courses('Git')

cool_student.grade_for_lecture(best_lector, 'Python', 10)
cool_student.grade_for_lecture(best_lector, 'Python', 10)
cool_student.grade_for_lecture(best_lector, 'Python', 10)

cool_student.grade_for_lecture(some_lecturer, 'Python', 9)
cool_student.grade_for_lecture(some_lecturer, 'Python', 10)
cool_student.grade_for_lecture(some_lecturer, 'Python', 10)

#
print(some_student.finished_courses)

print(some_lecturer.name)
print(some_lecturer.grades)
print(some_lecturer.courses_attached)

# Результат перегрузки метода __str__
print('')
print(some_student)
print('')
print(some_lecturer)
print('')
print(some_reviewer)



def average_grade_hw(student_list, course):
        total_grades = []
        for student in student_list:
            if course in student.courses_in_progress and student.grades.get(course) is not None:
                total_grades += student.grades.get(course)
        if sum(total_grades) != 0:
            print(f'Общая средняя оценка за дз по {course} : {round(sum(total_grades) / len(total_grades), 1)}')
        else:
          print('Нет оценок')


def average_grade_lecturer(lecturer_list, course):
        total_grades = []
        for lecturer in lecturer_list:
            if course in lecturer.courses_attached and lecturer.grades.get(course) is not None:
                total_grades += lecturer.grades.get(course)
        if sum(total_grades) != 0:
            print(f'Общая средняя оценка за лекции по {course} : {round(sum(total_grades) / len(total_grades), 1)}')
        else:
          print('Нет оценок')

average_grade_hw([best_student, some_student],'Python')
average_grade_hw([best_student, some_student],'Git')
average_grade_lecturer([best_lector,some_lecturer],'Python')
average_grade_lecturer([best_lector,some_lecturer],'Git')
