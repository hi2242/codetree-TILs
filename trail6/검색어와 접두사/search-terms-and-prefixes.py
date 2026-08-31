# 문제 정보
# 사전에 포함된 단어 n개
# 길이가 m인 문자열 S 검색
# 문자열 S에서 각 문자가 추가되는 순간 해당 검색어를 접두사로 하는 사전 내에 있는 서로 다른 단어의 수를 구해줌

# 입력 정보
# n -> 단어의 개수
# m -> 문자열의 길이
# strings -> 문자열들
# S -> 검색할 문자열

# 출력 정보
# S의 글자 하나씩 작성할 때마다 작성된 문자열을 prefix로 하는 사전 내에 서로 다른 단어의 수

# 풀이 순서

import sys

input = sys.stdin.readline

class Trie_Node:
    def __init__(self):
        self.count = 0
        self.end = False
        self.children = [None for _ in range(26)]

def init():
    for word in words:
        insert_node(word)

def insert_node(word):
    t = root
    for c in word:
        idx = ord(c) - ord("a")
        if t.children[idx] is None:
            t.children[idx] = Trie_Node()
        t.children[idx].count += 1
        t = t.children[idx]
    t.end = True

def search(word):
    t = root
    word_length = len(word)
    for i in range(word_length):
        idx = ord(word[i]) - ord("a")
        target = t.children[idx]
        if target is None:
            for j in range(i, word_length):
                print(0, end = " ")
            break
        print(target.count, end = " ")
        t = target

def solve():
    init()
    search(target)

root = Trie_Node()
n, m = map(int, input().split())
words = input().rstrip().split()
target = input().rstrip()
solve()
