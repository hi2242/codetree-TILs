import sys

input = sys.stdin.readline

# 선언부
def multi_input(n: int):
    return [input() for _ in range(n)]

# 입력부
N = int(input())
n_list = map(int, multi_input(N))

# 호출부
for i in n_list:
    if i % 2 == 1 and i % 3 == 0:
        print(i)