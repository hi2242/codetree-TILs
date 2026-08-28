# 문제 정보
# 루트 노드부터 리프 노드까지의 정보를 얻어냄
# 정보를 통해 트리 구조 파악
# 각 레벨은 --로 표현
# 한 노드에 여러 자식이 있으면 사전 순으로 가장 작은 것부터 출력

# 입력 정보
# n -> 입력할 줄의 개수
# k, x1, x2... -> 각 연결 정보
    # k -> 노드의 개수
    # x -> 노드의 이름

# 반환 정보
# 트리 정보

# 풀이 순서
# 1. 가상의 root를 만들어 여러 트리를 묶은 Trie를 만든다.
# 2. root부터 children을 정렬해서 dfs로 탐색하여 양식에 맞도록 출력한다.

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

class Trie_Node:
    def __init__(self):
        self.end = False
        self.children = {}

def init():
    for cmd in cmds:
        insert_node(cmd)

def insert_node(cmd):
    t = root
    for i in range(int(cmd[0])):
        target = t.children.get(cmd[i + 1])
        if target is None:
            t.children[cmd[i + 1]] = Trie_Node()
        t = t.children[cmd[i + 1]]
    t.end = True

def dfs(depth, parent):
    for c in sorted(parent.children.keys()):
        print(f"{'--' * depth if depth > 0 else ''}{c}")
        dfs(depth + 1, parent.children[c])

def solve():
    init()
    dfs(0, root)

n = int(input())
cmds = [input().rstrip().split() for _ in range(n)]
root = Trie_Node()
solve()
