import sys

input = sys.stdin.readline

# 선언부
def solve(m1: int, d1: int, m2: int, d2: int):
    day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    rev = False if m1 < m2 or (m1 == m2 and d1 <= d2) else True
    start_m, end_m = (m1, m2) if not rev else (m2, m1)
    start_d, end_d = (d1, d2) if not rev else (d2, d1)
    count = 0
    for i in range(start_m, end_m):
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
    count = count - start_d + end_d
    count = count if not rev else -count

    print(day_of_week[count % 7])

# 구현부
m1, d1, m2, d2 = map(int, input().split())
solve(m1, d1, m2, d2)
