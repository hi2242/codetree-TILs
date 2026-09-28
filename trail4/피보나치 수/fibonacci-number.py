import sys

input = sys.stdin.readline

def solve():
    dp = [0 for _ in range(46)]
    
    dp[1], dp[2] = 1, 1
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[N])

N = int(input())

solve()