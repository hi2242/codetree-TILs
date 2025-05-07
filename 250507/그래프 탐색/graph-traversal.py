# [0] 기본 정보
# N개의 정점과 M개의 간선인 양방향 그래프
# 1번 정점에서 시작
# 도달할 수 있는 서로 다른 정점의 수 (자기 자신에 도달하는 경우 제외)
def draw():
    for i in range(M):
        graph[line[i][0]].append(line[i][1])
        graph[line[i][1]].append(line[i][0])

def solve(e):
    global count

    for elem in graph[e]:
        if not visited[elem]:
            visited[elem] = 1
            count += 1
            solve(elem)

# 입력
# N(정점), M(간선)
# 간선 정보
# 1 <= N <= 1000
# 0 <= M <= min(10000, N(N-1) / 2)
# 1 <= x, y <= N
N, M = map(int, input().split())
line = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
visited[1] = 1
count = 0

# 출력
# 1번 정점에서 출발하여 도달할 수 있는 서로 다른 정점의 수 (1번 정점 제외)
draw()
solve(1)
print(count)