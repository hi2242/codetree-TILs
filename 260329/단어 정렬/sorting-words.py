import sys

input = sys.stdin.readline

# 선언부
def solve(s_list: list[str]):
    s_list.sort()
    print(*s_list, sep='\n')

# 구현부
n = int(input())
s_list = []
for _ in range(n):
    s_list.append(input().rstrip())
solve(s_list)
