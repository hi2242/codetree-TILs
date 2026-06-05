import sys

input = sys.stdin.readline

# 선언부
MAX_VALUE = 100

def solve():
    try:
        line_info.index(N)
        print("Yes")
    except ValueError:
        print("No")

# 구현부
N = int(input())
line_info = [0 for _ in range(MAX_VALUE + 1)]
for _ in range(N):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2 + 1):
        line_info[i] += 1
solve()
