import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    sorted_sum = sorted(students, key = lambda x: sum(x))
    for i in range(N):
        acc_money, count = (sorted_sum[i][0] // 2 + sorted_sum[i][1], 1) if sorted_sum[i][0] / 2 + sorted_sum[i][1] <= B else (0, 0)
        for j in range(N):
            if i == j:
                continue
            if acc_money + sum(sorted_sum[j]) > B:
                result = max(result, count)
                break
            acc_money += sum(sorted_sum[j])
            count += 1
    print(result)
    
# 구현부
N, B = map(int, input().split())
students = [tuple(map(int, input().split())) for _ in range(N)]
solve()
