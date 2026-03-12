import sys

input = sys.stdin.readline

# 선언부
def multi_input(n: int):
    return [input() for _ in range(n)]

# 입력부
n_list = list(map(int, multi_input(10)))

# 호출부
count = 0
for i in n_list:
    if i % 2 == 1:
        count += 1

print(count)