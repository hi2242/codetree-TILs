import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    target = s[1]
    temp = list(s)
    for i in range(len(temp)):
        if temp[i] == target:
            temp[i] = temp[0]

    print(*temp, sep='')
    
# 구현부
s = input().rstrip()
solve(s)
