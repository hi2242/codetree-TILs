import sys

input = sys.stdin.readline

# 선언부
def multi_input(n: int):
    return [input() for _ in range(n)]

# 입력부
n_list = list(map(int, multi_input(10)))

# 호출부
acc, count = 0, 0

for i in n_list:
    if 0 <= i <= 200:
        acc += i
        count += 1

print(f'{acc} {acc / count:.1f}')