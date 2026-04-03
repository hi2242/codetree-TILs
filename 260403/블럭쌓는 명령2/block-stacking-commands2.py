import sys

input = sys.stdin.readline

# 선언부
def solve(start: int, end: int, blocks: list[int]):
    for i in range(start, end + 1):
        blocks[i] += 1

# 구현부
N, K = map(int, input().split())
blocks = [0 for _ in range(N + 1)]
for _ in range(K):
    A, B = map(int, input().split())
    solve(A, B, blocks)
print(max(blocks))
