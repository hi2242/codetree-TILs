import sys

input = sys.stdin.readline

# 선언부
def solve(n: str, m: str):
    for i in range(len(n) - len(m) + 1):
        if n[i] == m[0]:
            for j in range(len(m)):
                if n[i + j] != m[j]:
                    break
            else:
                print(i)
                return
    else:
        print(-1)

# 구현부
N = input().rstrip()
M = input().rstrip()
solve(N, M)
