import sys

input = sys.stdin.readline

# 선언부
def move(target: list[int], v: int, t: int, curr_idx: int):
    for i in range(1, t + 1):
        target[curr_idx + i] = target[curr_idx + i - 1] + v

    return curr_idx + t

def solve():
    # 같 = 0, A = 1, B = 2
    state = -1
    count = 0
    for i in range(1, 1000001):
        if A[i] == 0:
            break
        if A[i] == B[i]:
            if state != 0:
                count += 1
            state = 0
        elif A[i] > B[i]:
            if state != 1:
                count += 1
            state = 1
        elif A[i] < B[i]:
            if state != 2:
                count += 1
            state = 2
    print(count)

# 구현부
N, M = map(int, input().split())
A, B = [0 for _ in range(1000001)], [0 for _ in range(1000001)]
curr_idx = 0
for _ in range(N):
    v, t = map(int, input().split())
    curr_idx = move(A, v, t, curr_idx)
curr_idx = 0
for _ in range(M):
    v, t = map(int, input().split())
    curr_idx = move(B, v, t, curr_idx)

solve()
    