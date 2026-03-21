import sys

input = sys.stdin.readline

# 선언부
def api(A_list: list[str], B: str):
    for i in range(len(A_list) - len(B) + 1):
        if A_list[i] == B[0]:
            for j in range(len(B)):
                if A_list[i + j] != B[j]:
                    break
            else:
                for k in range(len(B)):
                    A_list.pop(i)
                return 'continue'
    else:
        return 'break'

def solve(A: str, B: str):
    temp = list(A)
    while True:
        result = api(temp, B)

        if result == 'break':
            print(*temp, sep='')
            break
    
# 구현부
A = input().rstrip()
B = input().rstrip()
solve(A, B)
