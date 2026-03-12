import sys

input = sys.stdin.readline

# 선언부
def student_list(n: int):
    if n == 1:
        return 'John'
    elif n == 2:
        return 'Tom'
    elif n == 3:
        return 'Paul'
    elif n == 4:
        return 'Sam'
    else:
        return 'Vacancy'

# 입력부
while True:
    i = int(input())
    name = student_list(i)
    print(name)
    if name == 'Vacancy':
        break
# 호출부
