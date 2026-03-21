import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    temp = list(s)
    first_char, second_char = temp[0], temp[1]
    for i in range(len(temp)):
        if temp[i] == first_char:
            temp[i] = second_char
        elif temp[i] == second_char:
            temp[i] = first_char
    print(*temp, sep='')
    
# 구현부
s = input().rstrip()
solve(s)
