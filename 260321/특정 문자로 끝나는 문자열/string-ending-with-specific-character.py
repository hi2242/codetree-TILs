import sys

input = sys.stdin.readline

# 선언부
def multi_input(n: int):
    return [input().rstrip() for _ in range(n)]

def print_list(s_list: list[str]):
    if len(s_list):
        print(*s_list, sep='\n')
    else:
        print('None')

# 구현부
string_list = multi_input(10)
target = input().rstrip()
result = []
for s in string_list:
    if s[len(s) - 1] == target:
        result.append(s)
print_list(result)

