import sys

input = sys.stdin.readline

# 선언부
class Info1:
    def __init__(self, p: int, m: int, t: int) -> None:
        self.p, self.m, self.t = p, m, t

class Info2:
    def __init__(self, p: int, t: int) -> None:
        self.p, self.t = p, t

def solve():
    result = 0
    for i in range(1, M + 1):
        timeline = [0 for _ in range(N + 1)]
        for info in info1:
            if i != info.m:
                continue
            person = info.p
            timeline[person] = info.t if timeline[person] == 0 else min(timeline[person], info.t)
        for info in info2:
            person = info.p
            if timeline[person] == 0 or timeline[person] >= info.t:
                break
        else:
            count = 0
            for i in range(1, N + 1):
                if timeline[i]:
                    count += 1
            result = max(result, count)
    print(result)

# 구현부
N, M, D, S = map(int, input().split())
info1, info2 = [], []
for _ in range(D):
    p, m, t = map(int, input().split())
    info1.append(Info1(p, m, t))
for _ in range(S):
    p, t = map(int, input().split())
    info2.append(Info2(p, t))
solve()
