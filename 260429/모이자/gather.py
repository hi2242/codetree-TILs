import sys

input = sys.stdin.readline

# 선언부
def solve():
    distance_list = []
    for i in range(N):
        distance = 0
        for j in range(N):
            distance += human_count[j] * abs(j - i)
        distance_list.append(distance)
    print(min(distance_list))

# 구현부
N = int(input())
human_count = list(map(int, input().split()))
solve()
