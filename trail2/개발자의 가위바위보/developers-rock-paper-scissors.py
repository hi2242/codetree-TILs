import sys

input = sys.stdin.readline

def find_first_case():
    win = 0
    for i in range(N):
        if matches[i] in [[1, 2], [2, 3], [3, 1]]:
            win += 1
    return win

def find_second_case():
    win = 0
    for i in range(N):
        if matches[i] in [[2, 1], [3, 2], [1, 3]]:
            win += 1
    return win

# 선언부
def solve():
    print(max(find_first_case(), find_second_case()))
        
# 구현부
N = int(input())
matches = list(list(map(int, input().split())) for _ in range(N))
solve()
