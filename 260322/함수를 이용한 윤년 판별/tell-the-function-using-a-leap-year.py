import sys

input = sys.stdin.readline

# 선언부
def solve(year: int):
    if y % 100 == 0 and y % 400 != 0:
        print('false')
    elif y % 4 == 0:
        print('true')
    else:
        print('false')
        
# 구현부
y = int(input())
solve(y)
