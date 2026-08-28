# 문제 정보
# N개의 노드를 가진 트리
# 1번 노드가 루트 노드
# - 자신의 모든 자식 노드가 자신에게 값을 전파한 뒤에 값을 전파
# - 적혀있는 수가 양수일 경우, 부모 노드에 자신의 값을 더해줌
# - 양수가 아니면 아무것도 안함
# 1번 노드에 적힌 값은?

# 입력 정보
# N -> 노드의 개수
# t, a, p -> 노드의 정보
    # t -> 1이면 +a, 0이면 -a
    # p -> 부모 노드 정보

# 반환 정보
# answer -> 1번 노드에 적힌 값

# 풀이 순서
# 1. 노드 정보 트리에 저장
# 2. 노드 값을 부모로 전파

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, i, t, a, p):
        self.i = i
        self.a = a if t else -a
        self.p = p
        self.children = {}

def init():
    for i in range(2, len(nodes)):
        insert_node(nodes[i])

def insert_node(node):
    nodes[node.p].children[node.i] = node

def dfs(i):
    result = nodes[i].a
    if not len(nodes[i].children):
        return result
    for c in nodes[i].children.values():
        temp = dfs(c.i)
        result += temp if temp > 0 else 0
    return result
    

def solve():
    init()
    return dfs(1)

N = int(input())

root = Node(1, 1, 0, 0)
nodes = [0, root]
node_num = 2
for _ in range(N - 1):
    t, a, p = map(int, input().split())
    n = Node(node_num, t, a, p)
    nodes.append(n)
    node_num += 1

print(solve())
