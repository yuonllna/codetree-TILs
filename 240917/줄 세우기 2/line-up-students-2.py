class Student:
    def __init__(self, cm, kg, num):
        self.cm = cm
        self.kg = kg
        self.num = num
        
n = int(input())
students = []
for i in range(n):
    cm, kg = tuple(input().split())
    students.append(Student(int(cm), int(kg), i+1))


students.sort(key=lambda x: (x.cm, -x.kg))

for student in students:
   print(student.cm, student.kg, student.num)