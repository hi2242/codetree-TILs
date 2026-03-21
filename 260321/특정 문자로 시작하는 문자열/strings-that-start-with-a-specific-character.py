import sys

input = sys.stdin.readline

# 선언부
def multi_input(n: int):
    return [input().rstrip() for _ in range(n)]

def solve(string_list: list[str], target: str):
    count, length_sum = 0, 0
    for s in string_list:
        if s[0] == target:
            count += 1
            length_sum += len(s)

    print(f'{count} {length_sum / count:.2f}')
    
# 구현부
N = int(input())
string_list = multi_input(N)
target = input().rstrip()
solve(string_list, target)
