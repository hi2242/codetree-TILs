import sys

input = sys.stdin.readline

# 선언부
class Student:
    def __init__(self, number, height, weight):
        self.number = number
        self.height = height
        self.weight = weight

    def print(self):
        print(self.height, self.weight, self.number)

# 구현부
N = int(input())
student_list = []
for i in range(1, N + 1):
    h, w = map(int, input().split())
    student_list.append(Student(i, h, w))
student_list.sort(key = lambda x: (x.height, x.weight, -x.number), reverse = True)
for student in student_list:
    student.print()
    