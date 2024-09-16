class Student:
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg
        

students = []
for i in range(5):
    name, cm, kg = tuple(input().split())
    students.append(Student(name, int(cm), float(kg)))


students.sort(key=lambda x: (x.name))
print("name")
for student in students:
    print(student.name, student.cm, student.kg)
print("")
students.sort(key=lambda x: (-x.cm))
print("height")
for student in students:
   print(student.name, student.cm, student.kg)