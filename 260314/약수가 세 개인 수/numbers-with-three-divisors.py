import sys

input = sys.stdin.readline

# 선언부
def solve(start: int, end: int):
    count = 0
    for i in range(start, end + 1):
        temp_count = 0
        for j in range(2, i):
            if i % j == 0:
                temp_count += 1
        if temp_count == 1:
            count += 1
    return count
    
# 구현부
start, end = map(int, input().split())
print(solve(start, end))