import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if command[i] == 'C' and command[j] == 'O' and command[k] == 'W':
                    result += 1
    print(result)
    
# 구현부
N = int(input())
command = input().rstrip()
solve()
