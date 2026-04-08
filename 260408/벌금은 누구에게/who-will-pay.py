import sys

input = sys.stdin.readline

# 선언부
def solve(student_id: int):
    result = -1
    student_list[student_id] += 1
    if student_list[student_id] == K:
        result = student_id
    return result

# 구현부
N, M, K = map(int, input().split())
student_list = [0 for _ in range(N + 1)]

for _ in range(M):
    student_id = int(input())
    result = solve(student_id)
    if result != -1:
        print(result)
        break
else:
    print(result)
