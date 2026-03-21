import sys

input = sys.stdin.readline

# 선언부
def solve(s: str, target: str):
    target_idx = -1
    for i in range(len(s) - len(target) + 1):
        if s[i] == target[0]:
            for j in range(len(target)):
                if s[i + j] != target[j]:
                    break
            else:
                target_idx = i
                break
    print(target_idx)

# 구현부
s = input().rstrip()
target = input().rstrip()
solve(s, target)
