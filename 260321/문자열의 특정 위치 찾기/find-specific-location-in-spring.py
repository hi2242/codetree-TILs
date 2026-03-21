import sys

input = sys.stdin.readline

# 선언부

# 구현부
s, target = input().rstrip().split()
target_idx = s.find(target)
if target_idx == -1:
    print('No')
else:
    print(target_idx)
    