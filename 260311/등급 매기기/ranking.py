import sys

input = sys.stdin.readline

point = int(input())

grade = None

if point >= 90:
    grade = 'A'
elif point >= 80:
    grade = 'B'
elif point >= 70:
    grade = 'C'
elif point >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)