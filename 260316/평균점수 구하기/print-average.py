import sys

input = sys.stdin.readline

# 선언부

# 구현부
grade_list = list(map(float, input().split()))
print(f'{sum(grade_list) / 8:.1f}')