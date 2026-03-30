import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n1_list: list[int], n2_list: list[int]):
    result = 'Yes'
    t1_list, t2_list = sorted(n1_list), sorted(n2_list)
    for i in range(n):
        if t1_list[i] != t2_list[i]:
            result = 'No'
            break
    print(result)
    
# 구현부
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
solve(n, A, B)
