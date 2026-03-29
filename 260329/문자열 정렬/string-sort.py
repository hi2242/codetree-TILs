import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    result = ''
    alphabet = [0 for _ in range(26)]
    for c in s:
        alphabet[ord(c) - 97] += 1
    for i in range(26):
        result += chr(i + 97) * alphabet[i]
    print(result)
    
# 구현부
s = input().rstrip()
solve(s)
