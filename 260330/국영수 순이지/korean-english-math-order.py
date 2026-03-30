import sys

input = sys.stdin.readline

# 선언부
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = int(korean)
        self.english = int(english)
        self.math = int(math)

    def print(self):
        print(self.name, self.korean, self.english, self.math)

# 구현부
n = int(input())
student_list = []
for _ in range(n):
    name, korean, english, math = input().rstrip().split()
    student_list.append(Student(name, korean, english, math))

student_list.sort(key = lambda x: (x.korean, x.english, x.math), reverse = True)
for student in student_list:
    student.print()