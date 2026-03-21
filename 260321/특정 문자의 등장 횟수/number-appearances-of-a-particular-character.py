import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    count = [0, 0]
    for i in range(len(s) - 1):
        if s[i] == 'e':
            if s[i + 1] == 'e':
                count[0] += 1
            elif s[i + 1] == 'b':
                count[1] += 1
    print(*count)
    
# 구현부
s = input().rstrip()
solve(s)
