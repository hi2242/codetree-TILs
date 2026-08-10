# 문제 정보
# 1 ~ N 집합을 연산에 따라 진행

# 입력 정보
# N -> 정수의 개수
# M -> 연산의 횟수
# 0 a b -> a가 포함된 집합과 b가 포함된 집합을 합침, 이미 같은 집합이면 패스
# 1 a b -> a와 b가 같은 집합 안에 있다면 1, 아니면 0을 출력

# 반환 정보
# 1 a b 인 경우 알맞은 값을 반환

# 풀이 순서
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# print = sys.stdout.write

N, M = map(int, input().split())
command_list = [list(map(int, input().split())) for _ in range(M)]

def solution():
    s = [i for i in range(N + 1)]

    for command in command_list:
        query(command, s)

def union(s, a, b):
    root_a = find(s, a)
    root_b = find(s, b)
    if root_a == root_b:
        return
    s[root_a] = root_b

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def query(command, s):
    q, a, b = command
    if q == 0:
        union(s, a, b)
    else:
        root_a = find(s, a)
        root_b = find(s, b)
        print(int(root_a == root_b))

solution()
