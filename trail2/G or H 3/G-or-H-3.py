import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(1, 10001 - K):
        temp = 0
        for j in range(K + 1):
            temp += people[i + j]
        result = max(result, temp)
    print(result)

# 구현부
N, K = map(int, input().split())
people = [0 for _ in range(10001)]
for _ in range(N):
    line = input().rstrip().split()
    position, information = int(line[0]), line[1]
    point = 1 if information == 'G' else 2
    people[position] = point
solve()
