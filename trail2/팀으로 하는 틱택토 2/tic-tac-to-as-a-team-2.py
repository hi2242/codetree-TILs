import sys

input = sys.stdin.readline

# 선언부
def check_horizontal_vertical(result) -> None:
    for i in range(3):
        if len({numbers[i][j] for j in range(3)}) == 2:
            result.add(frozenset({numbers[i][j] for j in range(3)}))
        if len({numbers[j][i] for j in range(3)}) == 2:
            result.add(frozenset({numbers[j][i] for j in range(3)}))

def check_cross(result) -> None:
    if len({numbers[i][i] for i in range(3)}) == 2:
        result.add(frozenset({numbers[i][i] for i in range(3)}))
    if len({numbers[i][2 - i] for i in range(3)}) == 2:
        result.add(frozenset({numbers[i][2 - i] for i in range(3)}))

def solve():
    result = set()
    check_horizontal_vertical(result)
    check_cross(result)
    print(len(result))

# 구현부
numbers = [tuple(map(int, input().rstrip())) for _ in range(3)]
solve()
