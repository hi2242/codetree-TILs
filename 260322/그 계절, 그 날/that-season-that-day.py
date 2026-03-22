import sys

input = sys.stdin.readline

# 선언부
def is_leap(Y: int):
    if Y % 4 != 0 or (Y % 4 == 0 and Y % 100 == 0):
        return False
    else:
        return True

def end_day(M: int, leap: bool):
    if leap:
        if M == 2:
            return 29
        elif M <= 7:
            return 31 if M % 2 != 0 else 30
        else:
            return 30 if M % 2 != 0 else 31
    else:
        if M == 2:
            return 28
        elif M <= 7:
            return 31 if M % 2 != 0 else 30
        else:
            return 30 if M % 2 != 0 else 31

def print_season(M: int):
    if 3 <= M <= 5:
        print('Spring')
    elif 6 <= M <= 8:
        print('Summer')
    elif 9 <= M <= 11:
        print('Fall')
    else:
        print('Winter')

def solve(Y: int, M: int, D: int):
    leap = is_leap(Y)
    if D > end_day(M, leap):
        print(-1)
    else:
        print_season(M)

# 구현부
Y, M, D = map(int, input().split())
solve(Y, M, D)
