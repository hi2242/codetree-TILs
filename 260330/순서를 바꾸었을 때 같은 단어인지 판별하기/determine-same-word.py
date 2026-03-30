import sys

input = sys.stdin.readline

# 선언부
def solve(s1: str, s2: str):
    result = 'No'
    if sorted(s1) == sorted(s2):
        result = 'Yes'
    print(result)

# 구현부
s1 = input().rstrip()
s2 = input().rstrip()
solve(s1, s2)
