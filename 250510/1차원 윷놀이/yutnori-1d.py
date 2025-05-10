# [0] 기본 정보
# 번호(1 ~ M) 순서대로 연결

# [1] 말의 이동
# K개의 말이 1번 지점에 놓임
# N번의 턴
# 숫자에 따라 하나의 말을 선택해서 이동
# M까지 남은 칸 수보다 이동할 칸 수가 크다면 남은 칸 만큼만 이동

# [2] 점수 획득
# 이동한 말이 M번 지점에 도달하면 1점을 얻음
# M에 도달한 말을 선택할 순 있지만 변화는 없음
def solve(cnt):
    global count
    # 종료 조건

    if cnt == N:
        return

    for i in range(K):
        temp[i].append(move[cnt])
        solve(cnt + 1)
        t_count = 0
        for j in range(K):
            if sum(temp[j]) >= M - 1:
                t_count += 1

        count = max(count, t_count)
        temp[i].pop()

# 입력
# N(턴의 수), M(번호), K(말의 수)
# 각 턴 정보
# 1 <= N <= 12
# 2 <= M <= 100
# 1 <= K <= 4
# 1 <= 주어지는 수 <= 100
N, M, K = map(int, input().split())
move = list(map(int, input().split()))
result = [0 for _ in range(M)]
result[0] = K
temp = [[] for _ in range(K)]
count = 0

# 출력
# 최대 점수
solve(0)
print(count)