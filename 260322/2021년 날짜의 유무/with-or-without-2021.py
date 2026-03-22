import sys

input = sys.stdin.readline

# 선언부
def solve(M, D):
    if M <= 7:
        if M == 2:
            print('Yes' if D <= 28 else 'No')
        elif M % 2 != 0:
            print('Yes' if D <= 31 else 'No')
        else:
            print('Yes' if D <= 30 else 'No')
    else:
        if M % 2 != 0:
            print('Yes' if D <= 30 else 'No')
        else:
            print('Yes' if D <= 31 else 'No')

# 구현부
M, D = map(int, input().split())
solve(M, D)
