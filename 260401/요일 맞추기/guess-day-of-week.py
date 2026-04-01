import sys

input = sys.stdin.readline

# 선언부
def solve(m1: int, d1: int, m2: int, d2: int):
    day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    count = -1
    for i in range(m1, m2):
        if i <= 7:
            if i == 2:
                count += 28
            elif i % 2 == 0:
                count += 30
            else:
                count += 31
        else:
            if i % 2 == 0:
                count += 31
            else:
                count += 30
    count = count - (d1 - 1) + d2
    print(day_of_week[count % 7])

# 구현부
m1, d1, m2, d2 = map(int, input().split())
solve(m1, d1, m2, d2)
