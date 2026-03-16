import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    acc, count = 0, 0
    for n in n_list:
        if n == 0:
            break
        elif n % 2 == 0:
            acc += n
            count += 1

    print(count, acc)
    
# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
