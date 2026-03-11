import sys

input = sys.stdin.readline

student_id = int(input())

if student_id == 1:
    print('John')
elif student_id == 2:
    print('Tom')
elif student_id == 3:
    print('Paul')
else:
    print('Vacancy')