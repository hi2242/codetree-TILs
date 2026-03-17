import sys

input = sys.stdin.readline

# 선언부
def solve(q: list[int], n_list: list[int]):
    if q[0] == 1:
        print(n_list[q[1] - 1])
    elif q[0] == 2:
        if q[1] in n_list:
            print(n_list.index(q[1]) + 1)
        else:
            print(0)
    elif q[0] == 3:
        for i in range(q[1] - 1, q[2]):
            print(n_list[i], end=' ')
        print()

# 구현부
N, Q = map(int, input().split())
number_list = list(map(int, input().split()))
for _ in range(Q):
    question = list(map(int, input().split()))
    solve(question, number_list)