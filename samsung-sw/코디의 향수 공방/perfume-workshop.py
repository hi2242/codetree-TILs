# 문제 정보
# 향료는 고유한 번호를 가짐
# 향료는 무한 사용 가능

# [1] 향료 준비
# 1 ~ N 번호의 향료
# i번 향료의 향도는 Si
# 향료 준비는 가장 처음에 한 번만 주어짐

# [2] 향료 추가
# 추가되는 향료의 번호를 N + 1부터 부여
# 폐기된 번호는 재사용하지 않음
# 새로 추가된 향료의 향도는 v

# [3] 향료 폐기
# idx번 향료를 폐기
# 해당 향도 출력
# 폐기되었거나 존재하지 않는 번호면 -1 출력

# [4] 블렌딩
# 현재 사용 가능한 향료들 중에서 향도의 합이 정확히 K가 되도록 향료를 선택
# 필요한 향료의 최소 개수를 출력
# 같은 번호의 향료를 여러 번 사용 가능
# 만들 수 없다면 -1 출력

# [5] 향수 구성
# 향수는 탑노트 / 미들노트 / 베이스노트로 구성
# 각 노트에 향료를 하나씩 배치
# 세 향료의 향도 합이 K 이상이 되는 모든 경우의 수 출력
# 같은 번호의 향료를 여러 자리에 사용 가능
# 사용한 향료가 같더라도 배치한 자리가 다르면 서로 다른 경우

# 입력 정보
# Q -> 작업의 수
# 1 N S_1, S_2 ... S_N -> 향료 준비
# 2 v -> 향도 v인 향료 추가
# 3 idx -> idx번 향료 폐기
# 4 K -> 블렌딩 수행
# 5 K -> 향수 구성 수행

# 반환 정보
# 향료 폐기, 블렌딩, 향수 구성이 수행될 때마다 결과를 한 줄에 하나씩 출력

# 풀이 순서
# 1. 전역에 current_id를 1증가시키면서 현재까지 사용한 id값 저장
# 2. 향료 준비는 N개의 향료를 순회하며 딕셔너리에 추가
# 3. 향료 추가는 current_id 기반으로 딕셔너리에 추가
# 4. 향료 폐기는 idx가 flavors에 존재하는 지 확인 후 있으면 pop하고 향도 출력, 없으면 -1 출력
# 5. 블렌딩은 DP로 set에서 현재 향료들의 향도 중복 제거하여 K가 되도록 최소 향료 개수 계산 안되면 -1 출력
# 6. 향수 구성은 현재 사용 가능한 향료들을 오름차순으로 정렬하고 첫 번째 향료 고정 후 투 포인터로 나머지 두 개 찾기

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

INF = float('inf')

Q = int(input())
flavors = dict()
current_id = 0

def command(cmd):
    if cmd[0] == 1:
        prepare_flavors(cmd[1:])
    elif cmd[0] == 2:
        append_flavor(cmd[1])
    elif cmd[0] == 3:
        pop_flavor(cmd[1])
    elif cmd[0] == 4:
        blending(cmd[1])
    elif cmd[0] == 5:
        make_perfume(cmd[1])

def prepare_flavors(fs):
    global current_id
    for f in fs[1:]:
        current_id += 1
        flavors[current_id] = f

def append_flavor(v):
    global current_id
    current_id += 1
    flavors[current_id] = v

def pop_flavor(idx):
    if idx in flavors:
        print(flavors.pop(idx))
    else:
        print(-1)

def blending(k):
    if k == 0:
        print(0)
        return
    if not flavors:
        print(-1)
        return
        
    unique_flavors = set(flavors.values())
    dp = [INF] * (k + 1)
    dp[0] = 0
    
    for i in range(1, k + 1):
        for c in unique_flavors:
            if i >= c:
                if dp[i - c] + 1 < dp[i]:
                    dp[i] = dp[i - c] + 1
                    
    if dp[k] != INF:
        print(dp[k])
    else:
        print(-1)

def make_perfume(k):
    A = sorted(flavors.values())
    M = len(A)
    ans = 0
    
    for i in range(M):
        T = k - A[i]
        ptr = M - 1
        for j in range(M):
            while ptr >= 0 and A[j] + A[ptr] >= T:
                ptr -= 1
            ans += (M - 1 - ptr)
            
    print(ans)

for _ in range(Q):
    command_line = list(map(int, input().split()))
    command(command_line)