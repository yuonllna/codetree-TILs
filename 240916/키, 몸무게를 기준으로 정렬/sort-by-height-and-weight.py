class Student:
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg
        
n = int(input())
students = []
for i in range(n):
    name, cm, kg = tuple(input().split())
    students.append(Student(name, int(cm), int(kg)))


students.sort(key=lambda x: (x.cm, -x.kg))

for student in students:
   print(student.name, student.cm, student.kg)