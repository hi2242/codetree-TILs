import sys

input = sys.stdin.readline

# 선언부
def init():
    developer_info_list = [-1 for _ in range(N + 1)]
    developer_info_list[P] = K
    return developer_info_list

def inspect(a: int, b: int):
    if developer_info_list[a] == -1 and developer_info_list[b] == -1:
        return
    if developer_info_list[a] >= 1:
        developer_info_list[a] -= 1
        if developer_info_list[b] == -1:
            developer_info_list[b] = K
        elif developer_info_list[b] == 0:
            return
        else:
            developer_info_list[b] -= 1
    elif developer_info_list[b] >= 1:
        developer_info_list[b] -= 1
        if developer_info_list[a] == -1:
            developer_info_list[a] = K
        elif developer_info_list[a] == 0:
            return
        else:
            developer_info_list[a] -= 1
    
def solve():
    for i in range(T):
        inspect(inspect_info_list[i][1], inspect_info_list[i][2])

    for i in range(1, N + 1):
        if developer_info_list[i] != -1:
            print(1, end='')
        else:
            print(0, end='')

# 구현부
N, K, P, T = map(int, input().split())
inspect_info_list = []
developer_info_list = init()
for _ in range(T):
    inspect_info_list.append(list(map(int, input().split())))
inspect_info_list.sort(key = lambda x: x[0])
solve()
