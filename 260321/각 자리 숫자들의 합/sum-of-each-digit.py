import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    count = 0
    for c in s:
        count += int(c)
    print(count)
    
# 구현부
s = input().rstrip()
solve(s)
