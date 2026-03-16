import sys

input = sys.stdin.readline

# 구현부
def solve(n: int, g_list: list[float]):
    result = None
    avg = sum(g_list) / n
    if avg >= 4.0:
        result = 'Perfect'
    elif avg >= 3.0:
        result = 'Good'
    else:
        result = 'Poor'

    print(f'{avg:.1f}')
    print(result)

# 선언부
N = int(input())
grade_list = list(map(float, input().split()))
solve(N, grade_list)
