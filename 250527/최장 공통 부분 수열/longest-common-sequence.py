# [0] 기본 조건
# 길이가 N인 문자열 A
# 길이가 M인 문자열 B
# 공통 부분 수열 찾기

# [1] 공통 부분 수열
# "SABSBA", "ABABSA"가 있을 때
# "SSA"는 A의 부분 수열이지만 B의 부분 수열은 아니다.
# "ABA"는 A, B의 공통 부분 수열이다.
# "ABSA"는 A, B의 공통 부분 수열이다.
def print_grid(array):
    for row in array:
        print(*row)

    print()

def solve():
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(A)][len(B)]
# 입력
# A(문자열)
# B(문자열)
# 1 <= N, M <= 1000
# A, B는 알파벳 대문자로만 이루어짐
A = input()
B = input()
dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
# 출력
# 최대 공통 부분 수열
result = solve()
print(result)