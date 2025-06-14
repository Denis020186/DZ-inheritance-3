class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress or course not in lecturer.courses_attached:
            return 'Ошибка'
        if grade < 1 or grade > 10:
            return 'Ошибка'

        if hasattr(lecturer, 'grades'):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            lecturer.grades = {course: [grade]}
        return None

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"""Студент: 
Имя: {self.name} 
Фамилия: {self.surname}
Средняя оценка: {avg_grade}
Изучает: {courses_in_progress}
Завершил: {finished_courses}"""

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f"""Преподаватель:
Имя: {self.name}
Фамилия:{self.surname}""")


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return f"""Лектор: 
Имя:{self.name} 
Фамилия:{self.surname}
Средняя оценка за лекции: {avg_grade}"""

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создание объектов
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.grades = {'Python': [9, 10, 10]}

lecturer2 = Lecturer('Петр', 'Петров')
lecturer2.grades = {'Python': [8, 9, 9]}

reviewer = Reviewer('Сергей', 'Сергеев')

student1 = Student('Анна', 'Смирнова', 'female')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student1.grades = {'Python': [10, 9, 10]}

student2 = Student('Михаил', 'Петров', 'male')
student2.courses_in_progress = ['Python']
student2.finished_courses = ['Основы программирования']
student2.grades = {'Python': [8, 9, 9]}

# Вывод информации

print(reviewer)

print("")
print(lecturer1)
print("")
print(lecturer2)

print("")
print(student1)
print("")
print(student2)

# Сравнения
print("")
print("Результаты сравнений:")
print(f"Лектор 1 лучше лектора 2: {lecturer1 > lecturer2}")
print(f"Студент 1 лучше студента 2: {student1 > student2}")