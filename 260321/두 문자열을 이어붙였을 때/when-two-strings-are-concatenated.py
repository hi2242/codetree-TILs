import sys

input = sys.stdin.readline

# 선언부
def solve(s1: str, s2: str):
    if s1 == s2:
        print('true')
    else:
        print('false')
        
# 구현부
A = input().rstrip()
B = input().rstrip()
solve(A + B, B + A)
