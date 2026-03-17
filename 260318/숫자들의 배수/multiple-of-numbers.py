import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    count, temp = 0, 1
    n_list = []
    while True:
        if count == 2:
            print(*n_list)
            break
        current_number = n * temp
        n_list.append(n * temp)
        temp += 1
        if current_number and current_number % 5 == 0:
            count += 1

# 구현부
N = int(input())
solve(N)
