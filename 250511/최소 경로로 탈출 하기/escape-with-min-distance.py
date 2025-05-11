n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# N * M 크기의 grid
# 뱀이 있는 칸으로는 이동 불가
# (0, 0)부터 시작 (n - 1, m - 1)로 탈출
import sys
from collections import deque

input = sys.stdin.readline

def solve(array):
    # n * m의 grid를 만드려면 처리 순서가 바깥부터인 점을 유의한다.
    visited = [[0 for _ in range(m)] for _ in range(n)]
    d = deque()
    count = 0
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    d.append((0, 0))
    visited[0][0] = 1
    
    while d:
        dx, dy = d.popleft()
        
        for nx, ny in move:
            if 0 <= dx + nx < n and 0 <= dy + ny < m and visited[dx + nx][dy + ny] == 0 and array[dx + nx][dy + ny] != 0:
                d.append((dx + nx, dy + ny))
                visited[dx + nx][dy + ny] = visited[dx][dy] + 1

    return visited

result = solve(a)

if result[n - 1][m - 1] == 0:
    print(-1)
else:
    print(result[n - 1][m - 1] - 1)