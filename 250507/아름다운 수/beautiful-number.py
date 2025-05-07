# [0] 기본 조건
# 숫자(1 ~ 4)

# [1] 아름다운 수
# 숫자가 해당 숫자만큼 반복되는 수
# ex) 1333221 -> 아름다운 수 (1 * 1, 3 * 3, 2 * 2, 1 * 1)
# ex) 111, 22222222 -> 아름다운 수 (1 * 1이 세번, 2 * 2가 네번)
# ex) 222 -> 아름다운 수 X (2 * 2 한번 이후 2 * 1이라 규칙 위배)
def solve(num, cnt):
    global count
    # 종료 조건
    if cnt == N:
        count += 1
        return

    for i in range(1, 5):
        if cnt + i > N:
            continue

        for _ in range(i):
            result.append(i)
        solve(i, cnt + i)
        for _ in range(i):
            result.pop()

# 입력
# N(정수)
# 1 <= N <= 10
N = int(input())
result = []
count = 0

# 출력
# N자리 아름다운 수의 개수 출력
for i in range(1, 5):
    for _ in range(i):
        result.append(i)
    solve(i, i)
    for _ in range(i):
        result.pop()

print(count)