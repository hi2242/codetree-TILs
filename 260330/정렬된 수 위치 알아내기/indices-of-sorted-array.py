import sys

input = sys.stdin.readline

# 선언부
class Element:
    def __init__(self, value, index):
        self.value = value
        self.index = index
    
    def print(self):
        print(self.index, end=' ')

def solve(n: int, e_list: list[Element]):
    answer = [0 for _ in range(N)]
    for i in range(N):
        answer[element_list[i].index] = i + 1
    print(*answer)

# 구현부
N = int(input())
n_list = list(map(int, input().split()))
element_list = []

for i in range(N):
    element_list.append(Element(n_list[i], i))
element_list.sort(key = lambda x: (x.value, x.index))

solve(N, element_list)
