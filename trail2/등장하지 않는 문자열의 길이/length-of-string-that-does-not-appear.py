import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            temp = 0
            if string[i] == string[j]:
                for k in range(N):
                    ni, nj = i + k, j + k
                    if 0 <= nj < N and string[ni] == string[nj]:
                        temp += 1
                    else:
                        break
            result = max(result, temp)
    print(result + 1)

# 구현부
N = int(input())
string = input().rstrip()
solve()
