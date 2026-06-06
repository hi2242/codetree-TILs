import sys

input = sys.stdin.readline

# 선언부
def solve():
    count = 0
    for gugu, pos in positions:
        if gugus[gugu] == -1:
            gugus[gugu] = pos
        elif gugus[gugu] != pos:
            count += 1
            gugus[gugu] = pos
    print(count)
    
# 구현부
N = int(input())
gugus = [-1 for _ in range(11)]
positions = [tuple(map(int, input().split())) for _ in range(N)]
solve()
