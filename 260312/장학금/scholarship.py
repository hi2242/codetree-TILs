import sys

input = sys.stdin.readline

midterm_point, finalterm_point = map(int, input().split())

def scholarship(mid_point: int, final_point: int):
    if mid_point < 90:
        return 0

    if final_point >= 95:
        return 100000
    elif final_point >= 90:
        return 50000
    return 0

print(scholarship(midterm_point, finalterm_point))
