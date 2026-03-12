import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
for i in range(N, 101):
    grade = None
    if i >= 90:
        grade = 'A'
    elif i >= 80:
        grade = 'B'
    elif i >= 70:
        grade = 'C'
    elif i >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(grade, end=' ')