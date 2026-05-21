import sys

input = sys.stdin.readline

DIGIT = 3
RANGE = 2

# 선언부
def make_grid(numbers: list[int]) -> list[list[int]]:
    grid = [[] for _ in range(DIGIT)]
    for i in range(DIGIT):
        for j in range(-RANGE, RANGE + 1):
            temp = N[(numbers[i] + j - 1) % len(N)]
            if temp not in grid[i]:
                grid[i].append(temp)
    return grid

def calc_acc(grid: list[list[int]]) -> int:
    acc = 1
    for i in range(DIGIT):
        acc *= len(grid[i])
    return acc

def calc_redundancy(f_grid: list[list[int]], s_grid: list[list[int]]) -> int:
    result = [0 for _ in range(DIGIT)]
    acc = 1
    for i in range(DIGIT):
        for j in range(len(f_grid[i])):
            if f_grid[i][j] in s_grid[i]:
                result[i] += 1
    for i in range(DIGIT):
        acc *= result[i]
    return acc

def solve():
    result = 0
    first_grid, second_grid = make_grid(first_numbers), make_grid(second_numbers)
    result += calc_acc(first_grid)
    result += calc_acc(second_grid)
    result -= calc_redundancy(first_grid, second_grid)
    print(result)

# 구현부
N = [i for i in range(1, int(input()) + 1)]
first_numbers = list(map(int, input().split()))
second_numbers = list(map(int, input().split()))
solve()
