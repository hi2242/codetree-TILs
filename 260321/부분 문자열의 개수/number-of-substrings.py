import sys

input = sys.stdin.readline

# 선언부
def solve(s: str, target: str):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == target[0] and s[i + 1] == target[1]:
            count += 1
    print(count)

# 구현부
A = input().rstrip()
B = input().rstrip()
solve(A, B)
