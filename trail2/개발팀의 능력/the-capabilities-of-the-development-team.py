import sys

input = sys.stdin.readline

DEVELOPERS_NUM = 5
# 선언부
def calc_diff(i: int, j: int, k: int, l: int) -> int:
    team_point = [
        developers[i] + developers[j],
        developers[k] + developers[l],
        sum(developers) - (developers[i] + developers[j] + developers[k] + developers[l])
    ]
    if len(set(team_point)) != 3:
        return int(1e9)
    return max(team_point) - min(team_point)

def solve():
    result = int(1e9)
    for i in range(DEVELOPERS_NUM):
        for j in range(DEVELOPERS_NUM):
            for k in range(DEVELOPERS_NUM):
                for l in range(DEVELOPERS_NUM):
                    if len({i, j, k, l}) != 4:
                        continue
                    result = min(result, calc_diff(i, j, k, l))
    print(-1 if result == int(1e9) else result)

# 구현부
developers = list(map(int, input().split()))
solve()
