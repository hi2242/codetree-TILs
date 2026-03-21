import sys

input = sys.stdin.readline

# 선언부
def solve(s_list: list[str]):
    s = ''
    for each in s_list:
        s += each

    for i in range(len(s)):
        print(s[i], end='')
        if not (i + 1) % 5:
            print()

# 구현부
N = int(input())
string_list = input().rstrip().split()
solve(string_list)
