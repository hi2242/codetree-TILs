import sys

input = sys.stdin.readline

# 선언부
class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

    def print(self):
        print(self.height, self.weight, self.number)

# 구현부
N = int(input())
student_list = []
for i in range(1, N + 1):
    h, w = map(int, input().split())
    student_list.append(Student(h, w, i))

student_list.sort(key = lambda x: (x.height, -x.weight))
for student in student_list:
    student.print()
    