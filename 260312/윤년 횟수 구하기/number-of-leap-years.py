import sys

input = sys.stdin.readline

# 선언부
def check_leap_year(year: int):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True

# 입력부
N = int(input())

# 호출부
count = 0
for i in range(1, N + 1):
    if check_leap_year(i):
        count += 1

print(count)