import sys

input = sys.stdin.readline

# 선언부
def solve(a: int, b: int):
    modulo_list = [0 for _ in range(10)]
    acc = 0
    while a > 1:
        modulo_list[a % b] += 1
        a = a // b

    for i in range(10):
        if modulo_list[i]:
            acc += modulo_list[i] ** 2

    print(acc)
    
# 호출부
A, B = map(int, input().split())
solve(A, B)
