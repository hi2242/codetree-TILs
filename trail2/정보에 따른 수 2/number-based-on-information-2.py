import sys

input = sys.stdin.readline

MIN_L = 1
MAX_L = 1000
# 선언부
def solve():
    result = 0
    for i in range(a, b + 1):
        distance_S, distance_N = -1, -1
        for j in range(MAX_L):
            if MIN_L <= i + j <= MAX_L:
                if distance_S == -1 and info[i + j] == 'S':
                    distance_S = j
                if distance_N == -1 and info[i + j] == 'N':
                    distance_N = j
            if MIN_L <= i - j <= MAX_L:
                if distance_S == -1 and info[i - j] == 'S':
                    distance_S = j
                if distance_N == -1 and info[i - j] == 'N':
                    distance_N = j
        if distance_S <= distance_N:
            result += 1
    print(result)

# 구현부
T, a, b = map(int, input().split())
info = ['' for _ in range(MAX_L + 1)]
for _ in range(T):
    alphabet, p = input().rstrip().split()
    info[int(p)] = alphabet
solve()
