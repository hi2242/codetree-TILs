import sys

input = sys.stdin.readline

# 선언부
class Student:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.point = int(subject1) + int(subject2) + int(subject3)
    
    def print(self):
        print(self.name, self.subject1, self.subject2, self.subject3)

# 구현부
N = int(input())
student_list = []
for _ in range(N):
    name, subject1, subject2, subject3 = input().rstrip().split()
    student_list.append(Student(name ,subject1, subject2, subject3))
student_list.sort(key = lambda x: x.point)
for student in student_list:
    student.print()
