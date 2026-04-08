import sys

input = sys.stdin.readline

# 선언부
def solve(target: str, curr_idx: int, d: str, t: int):
    for k in range(t):
        if d == 'R':
            curr_idx += 1
        else:
            curr_idx -= 1
        if target == 'A':
            A.append(curr_idx)
        else:
            B.append(curr_idx)
        
    return curr_idx

# 구현부
N, M = map(int, input().split())
A = [0]
B = [0]
curr_idx = 0
for i in range(N):
    line = input().rstrip().split()
    d, t = line[0], int(line[1])
    curr_idx = solve('A', curr_idx, d, t)
curr_idx = 0
for i in range(M):
    line = input().rstrip().split()
    d, t = line[0], int(line[1])
    curr_idx = solve('B', curr_idx, d, t)
time = 1
while True:
    if time == len(A):
        print(-1)
        break
    if A[time] == B[time]:
        print(time)
        break
    time += 1