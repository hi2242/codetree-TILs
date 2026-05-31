import sys

input = sys.stdin.readline

# 선언부
INF = float('inf')

def calc_distance(i, j):
    result = INF
    for k in range(N):
        if k == i or k == j or string_number[k] == "1":
            for l in range(k + 1, N):
                if l == i or l == j or string_number[l] == "1":
                    result = min(result, l - k)
                    break
    return result

def solve():
    result = 0
    for i in range(N):
        if string_number[i] == "1":
            continue
        for j in range(i + 1, N):
            if string_number[j] == "1":
                continue
            result = max(result, calc_distance(i, j))
    print(result)

# 구현부
N = int(input())
string_number = input().rstrip()
solve()
