import sys

input = sys.stdin.readline

# 선언부

# 구현부
s1, s2 = input().rstrip().split()
print('same' if len(s1) == len(s2) else f'{s1} {len(s1)}' if len(s1) > len(s2) else f'{s2} {len(s2)}')