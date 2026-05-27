import sys

input = sys.stdin.readline

# 선언부
INF = float('inf')

def solve():
    result = 0
    for i in range(N):
        if string[i] == '1':
            continue
        temp = INF
        for j in range(N):
            for k in range(j + 1, N):
                if (i == j or string[j] == '1') and (i == k or string[k] == '1'):
                    temp = min(temp, abs(j - k))
        result = max(result, temp)
    print(result)

# 구현부
N = int(input())
string = input().rstrip()
solve()
