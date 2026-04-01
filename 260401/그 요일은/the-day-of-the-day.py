import sys

input = sys.stdin.readline

# 선언부
def calculate_day(m: int, d: int):
    day_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0
    for i in range(1, m):
        count += day_list[i]
    count += d
    return count

def solve(m1: int, d1: int, m2: int, d2: int, day_info: str):
    result = 0
    day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    count1, count2 = calculate_day(m1, d1), calculate_day(m2, d2)
    count = (count2 - count1)
    idx = day_of_week.index(day_info)

    result += count // 7
    if count % 7 >= idx:
        result += 1
    print(result)
    
# 구현부
m1, d1, m2, d2 = map(int, input().split())
day_info = input().rstrip()
solve(m1, d1, m2, d2, day_info)
