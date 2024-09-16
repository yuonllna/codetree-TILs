class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = []
for i in range(n):
    kor, eng, math = tuple(input().split())
    students.append(Student(kor, eng, math))


students.sort(key=lambda x: (x.kor, x.eng, x.math))

for student in students: 
    print(student.kor, student.eng, student.math)