class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 < grade <= 5:
            self.grades.append(grade)
        else:
            raise(ValueError("Оценка должна быть от 1 до 5"))

    def average_grade(self):
        if len(self.grades) != 0:
            return sum(self.grades) / len(self.grades)
        else:
            return "Оценок нет"


if __name__ == '__main__':
    student = Student('Maxim')
    student.add_grade(4)
    student.add_grade(3)
    print(student.average_grade())
