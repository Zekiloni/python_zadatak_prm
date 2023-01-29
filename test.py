

students = []

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        students.append(self)


name = input('Unesite ime studenta: ')
grade = int(input('Unesite ocenu studenta: '))

newStudent = Student(name, grade)

print('Unešen student: ' + newStudent.name)
