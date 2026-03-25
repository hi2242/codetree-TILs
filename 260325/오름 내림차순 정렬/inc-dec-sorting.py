import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n_list: list[int], option: str):
    temp = [n for n in n_list]
    if option == 'ASC':
        for i in range(n):
            minimum, min_idx = int(1e9), None
            for j in range(i + 1, n):
                if temp[j] < minimum:
                    minimum, min_idx = temp[j], j
            else:
                if temp[i] > minimum:
                    temp[i], temp[min_idx] = temp[min_idx], temp[i]
    elif option == 'DESC':
        for i in range(n):
            maximum, max_idx = -int(1e9), None
            for j in range(i + 1, n):
                if temp[j] > maximum:
                    maximum, max_idx = temp[j], j
            else:
                if temp[i] < maximum:
                    temp[i], temp[max_idx] = temp[max_idx], temp[i]
    print(*temp)

# 구현부
n = int(input())
number_list = list(map(int, input().split()))
solve(n, number_list, 'ASC')
solve(n, number_list, 'DESC')
