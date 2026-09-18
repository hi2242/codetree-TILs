# 문제 정보
# n개의 정점, m개의 간선으로 이루어진 양방향 그래프
# k개의 점이 순서대로 주어지면 그래프에서 순서대로 이동이 가능한지 판단

# 입력 정보
# n -> 정점의 수
# m -> 간선의 수
# k -> 순서의 길이
# (x, y) -> 정점 연결 정보
# 마지막 줄 -> k개의 점으로 이루어진 순서 정보

# 반환 정보
# 가능 여부 -> 1(가능), 0(불가능)

# 풀이 순서
# 1. 접근 가능한 정점은 set으로 저장
# 2. 그래프의 양쪽을 합칠 때는 각자의 요소를 update
# 3. 있는지 여부를 통해 이동 가능한지 판단

import sys

input = sys.stdin.readline

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    parents[root_a] = root_b

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def solve():
    if k == 1:
        return 1

    for i in range(len(path) - 1):
        root_a = find(path[i])
        root_b = find(path[i + 1])
        if root_a != root_b:
            return 0
    return 1

n, m, k = map(int, input().split())

parents = [i for i in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

path = list(map(int, input().split()))
print(solve())
