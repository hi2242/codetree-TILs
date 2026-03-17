import sys

input = sys.stdin.readline

# 선언부
def solve(first: int, second: int):
    n_list = [first, second]
    for i in range(2, 10):
        n_list.append(n_list[i - 1] + 2 * n_list[i - 2])

    print(*n_list)
    
# 구현부
first, second = map(int, input().split())
solve(first, second)
