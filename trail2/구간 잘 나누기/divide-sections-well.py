import sys

input = sys.stdin.readline

# 선언부
MAX_RANGE = 5000
def solve():
    for i in range(1, MAX_RANGE + 1):
        last_index = -1
        for j in range(M):
            temp = i
            for k in range(last_index + 1, N):
                if temp >= numbers[k]:
                    temp -= numbers[k]
                    last_index = k
                else:
                    last_index = last_index
                    break
            else:
                print(i)
                return
            

# 구현부
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
solve()
