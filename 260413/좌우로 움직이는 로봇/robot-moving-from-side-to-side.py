import sys

input = sys.stdin.readline

# 선언부
def move(target: list[int], t: int, d: str):
    diff = 1 if d == 'R' else -1
    for _ in range(t):
        target.append(target[-1] + diff)

def flat(target: list[int], length: int):
    for _ in range(length):
        target.append(target[-1])

def solve():
    count = 0
    for i in range(1, len(A)):
        if A[i] == B[i] and A[i - 1] != B[i - 1]:
            count += 1

    print(count)

# 구현부
N, M = map(int, input().split())
A, B = [0], [0]

for _ in range(N):
    t, d = input().rstrip().split()
    move(A, int(t), d)
for _ in range(M):
    t, d = input().rstrip().split()
    move(B, int(t), d)
flat(A if len(A) < len(B) else B, abs(len(A) - len(B)))
solve()
