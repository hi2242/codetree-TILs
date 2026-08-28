# 문제 정보
# N개의 수열이 주어진다.
# 임의의 수열 A가 다른 어떠한 수열 B의 접두사가 되는지 판단한다.
# 단, 이 문제에서는 정확히 일치하는 두 수열에 대해 접두사라 판단하지 않는다.

# 입력 정보
# N -> 수열의 수
# numbers -> 수열에 대한 2차원 배열

# 반환 정보
# 임의의 수열 A가 다른 수열 B의 접두사가 된다면 0, 그런 B가 없다면 1을 출력

# 풀이 순서
# 1. 각 수열을 Trie 자료구조에 등록한다.
# 2. 다시 수열을 돌면서 조건에 맞는 수열이 있다면 0을 출력하고 종료한다. (도착 노드의 자식이 있다면 prefix라는 정보를 활용)

import sys

input = sys.stdin.readline

class Trie_Node:
    def __init__(self):
        self.end = False
        self.children = {}

def init():
    for numbers in numbers_list:
        insert_node(numbers)

def insert_node(numbers):
    t = root
    for number in numbers:
        target = t.children.get(number)
        if target is None:
            t.children[number] = Trie_Node()
        t = t.children[number]
    t.end = True

def find(numbers):
    t = root
    for number in numbers:
        if t.end:
            return True
        t = t.children[number]
    return False

def solve():
    result = 1
    init()
    for numbers in numbers_list:
        if find(numbers):
            result = 0
            break
    return result

N = int(input())
numbers_list = [list(input().rstrip()) for _ in range(N)]
root = Trie_Node()
print(solve())