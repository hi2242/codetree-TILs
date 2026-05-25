import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    prices.sort()
    for i in range(N):
        acc_price = prices[i] / 2
        temp = 1 if prices[i] / 2 <= B else 0
        for j in range(N):
            if i == j:
                continue
            if acc_price + prices[j] > B:
                break
            acc_price += prices[j]
            temp += 1
        result = max(result, temp)
    print(result)

# 구현부
N, B = map(int, input().split())
prices = [int(input()) for _ in range(N)]
solve()
