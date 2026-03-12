import sys

input = sys.stdin.readline

# 선언부
def multi_input(n: int):
    return [input() for _ in range(n)]

# 입력부
N = int(input())
n_list = list(map(int, multi_input(N)))

# 호출부
acc, count = 0, 0

for i in n_list:
    acc += i
    count += 1

print(f'{acc} {acc / count:.1f}')