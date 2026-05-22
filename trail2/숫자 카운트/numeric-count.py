import sys

input = sys.stdin.readline

DIGIT = 3

# 선언부
def init() -> list[int]:
    result = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if len({i, j, k}) == DIGIT:
                    result.append(i * 100 + j * 10 + k)
    return result

def check_f_count(k: int, question: int, f_count: int) -> bool:
    k_position, q_position = [k // 100, k // 10 % 10, k % 10], [question // 100, question // 10 % 10, question % 10]
    count = 0
    for i in range(DIGIT):
        count += k_position[i] == q_position[i]
    return count == f_count

def check_s_count(k: int, question: int, s_count: int) -> bool:
    k_position, q_position = [k // 100, k // 10 % 10, k % 10], [question // 100, question // 10 % 10, question % 10]
    count = 0
    for i in range(DIGIT):
        for j in range(DIGIT):
            if i == j:
                continue
            count += k_position[i] == q_position[j]
    return count == s_count

def solve():
    result = init()
    for i in range(N):
        question, f_count, s_count = command_list[i]
        temp = []
        for k in result:
            if check_f_count(k, question, f_count) and check_s_count(k, question, s_count):
                temp.append(k)
        result = temp
    print(len(result))

# 구현부
N = int(input())
command_list = [list(map(int, input().split())) for _ in range(N)]
solve()
