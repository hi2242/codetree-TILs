import sys

input = sys.stdin.readline

DEVELOPERS_NUM = 6

# 선언부
def solve():
    result = int(1e9)
    for i in range(DEVELOPERS_NUM):
        for j in range(DEVELOPERS_NUM):
            for k in range(DEVELOPERS_NUM):
                for l in range(DEVELOPERS_NUM):
                    if len({i, j, k, l}) != 4:
                        continue
                    max_point = max(developers[i] + developers[j], developers[l] + developers[k], sum(developers) - (developers[i] + developers[j] + developers[l] + developers[k]))
                    min_point = min(developers[i] + developers[j], developers[l] + developers[k], sum(developers) - (developers[i] + developers[j] + developers[l] + developers[k]))
                    result = min(result, max_point - min_point)
    print(result)

# 구현부
developers = list(map(int, input().split()))
solve()
