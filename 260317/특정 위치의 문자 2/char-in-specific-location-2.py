import sys

input = sys.stdin.readline

# 선언부
def solve(s_list: list[int]):
    print(s_list[1], s_list[4], s_list[7])

# 구현부
string_list = input().split()
solve(string_list)
