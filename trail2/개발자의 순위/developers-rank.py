import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(1, N + 1):
        info = [1 for _ in range(N + 1)]
        info[0] = 0
        for r in rounds:
            temp = 0
            for j in r:
                if i == j:
                    info[j] = 0
                    break
                info[j] = temp
        result += info.count(1)
    print(result)

# 구현부
K, N = map(int, input().split())
rounds = [tuple(map(int, input().split())) for _ in range(K)]
solve()
