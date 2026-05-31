import sys
import heapq

input = sys.stdin.readline

# 선언부
INF = float('inf')

def init(start):
    q = []
    visited = [0 for _ in range(N + 1)]
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    heapq.heappush(q, (0, start))

    return q, visited, distance

def dijkstra(start):
    q, visited, distance = init(start)

    while q:
        dist, curr = heapq.heappop(q)
        if visited[curr]:
            continue
        visited[curr] = 1

        for e, w in graph[curr]:
            cost = dist + w
            if cost < distance[e]:
                distance[e] = min(distance[e], cost)
                heapq.heappush(q, (cost, e))
        
    return distance

def solve():
    result = dijkstra(1)
    for i in range(2, N + 1):
        print(result[i] if result[i] != INF else -1)


# 구현부
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
solve()
