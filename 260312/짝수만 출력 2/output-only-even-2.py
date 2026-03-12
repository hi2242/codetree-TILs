import sys

input = sys.stdin.readline

# 선언부

# 입력부
B, A = map(int, input().split())

# 호출부
while B >= A:
    print(B, end=' ')
    B -= 2