import sys

input = sys.stdin.readline

# 선언부
string_list = ['L', 'E', 'B', 'R', 'O', 'S']
def solve(s: str):
    if s not in string_list:
        print('None')
    else:
        print(string_list.index(s))

# 호출부
s = input().rstrip()
solve(s)
