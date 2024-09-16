class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = []
for i in range(n):
    name, kor, eng, math = tuple(input().split())
    students.append(Student(name, kor, eng, math))


students.sort(key=lambda x: (x.kor, x.eng, x.math), reverse=True)

for student in students: 
    print(student.name, student.kor, student.eng, student.math)