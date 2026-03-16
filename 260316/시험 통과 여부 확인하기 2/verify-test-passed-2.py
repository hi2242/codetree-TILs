import sys

input = sys.stdin.readline

# 구현부
def solve(grade_list: list[int]):
    avg = sum(grade_list) / 4
    if avg >= 60:
        return 'pass'
    return 'fail'

# 선언부
N = int(input())
count = 0
for _ in range(N):
    student_grade = list(map(int, input().split()))
    result = solve(student_grade)
    print(result)
    if result == 'pass':
        count += 1
print(count)
