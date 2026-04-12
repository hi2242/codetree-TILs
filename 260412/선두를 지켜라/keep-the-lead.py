import sys

input = sys.stdin.readline

# 선언부
def move(target: str, v: int, t: int):
    for _ in range(t):
        if target == 'A':
            A.append(A[-1] + v)
        else:
            B.append(B[-1] + v)

def solve():
    is_top_A = -1
    result, i = 0, 0
    while True:
        if i == len(A):
            break
        if A[i] > B[i]:
            is_top_A = True
            break
        elif A[i] < B[i]:
            is_top_A = False
            break
        else:
            i += 1

    if is_top_A == -1:
        print(result)
    else:
        for j in range(i + 1, len(A)):
            if is_top_A == False and A[j] > B[j]:
                is_top_A = True
                result += 1
            elif is_top_A == True and A[j] < B[j]:
                is_top_A = False
                result += 1
        print(result)

# 구현부
N, M = map(int, input().split())
A, B = [0], [0]
for _ in range(N):
    v, t = map(int, input().split())
    move('A', v, t)
for _ in range(M):
    v, t = map(int, input().split())
    move('B', v, t)
solve()
