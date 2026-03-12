import sys

input = sys.stdin.readline

# 선언부
def program(n: int):
    if n < 25:
        return 'Higher'
    elif n > 25:
        return 'Lower'
    else:
        return 'Good'

# 입력부
while True:
    i = int(input())
    result = program(i)
    print(result)
    if result == 'Good':
        break

# 호출부
