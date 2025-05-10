# [0] 기본 정보
# 2N개의 정수 수열 A
# 각각 N개씩 2개의 그룹으로 나눔
# 각 그룹 원소합의 차가 최소가 되도록
def divide(T):
    temp_C = A.copy()
    for t in T:
        if t in temp_C:
            temp_C.remove(t)

    return temp_C

def compare(a, b):
    global count

    if count == -1:
        count = abs(sum(a) - sum(b))

    else:
        count = min(count, abs(sum(a) - sum(b)))

def solve(cnt, curr_num):
    # 종료 조건
    if cnt == N:
        compare(temp_B, divide(temp_B))
        return

    for i in range(curr_num + 1, 2 * N):
        temp_B.append(A[i])
        solve(cnt + 1, i)
        temp_B.pop()

# 입력
# N(정수)
# A(정수 수열)
# 1 <= N <= 10
# 1 <= 주어지는 수 <= 1000
N = int(input())
A = list(map(int, input().split()))
temp_B = []
count = -1

# 출력
# 두 부분집합의 차이
temp_B.append(A[0])
solve(1, 0)
temp_B.pop()
print(count)
