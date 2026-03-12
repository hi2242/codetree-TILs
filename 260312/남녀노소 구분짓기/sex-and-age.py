import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input() for _ in range(n)]

gender, age = map(int, multi_input(2))

if gender == 0:
    if age >= 19:
        print('MAN')
    else:
        print('BOY')
else:
    if age >= 19:
        print('WOMAN')
    else:
        print('GIRL')