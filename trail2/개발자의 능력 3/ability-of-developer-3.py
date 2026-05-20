import sys

input = sys.stdin.readline

# 선언부
def solve():
    diff = int(1e9)
    for i in range(4):
        for j in range(i + 1, 5):
            for k in range(j + 1, 6):
                team_a = numbers[i] + numbers[j] + numbers[k]
                team_b = sum(numbers) - team_a
                diff = min(diff, abs(team_a - team_b))
    print(diff)

# 구현부
numbers = list(map(int, input().split()))
solve()
