# 문제 정보
# 1 ~ N 집합을 연산에 따라 진행

# 입력 정보
# N -> 정수의 개수
# M -> 연산의 횟수
# 0 a b -> a가 포함된 집합과 b가 포함된 집합을 합침, 이미 같은 집합이면 패스
# 1 a b -> a와 b가 같은 집합 안에 있다면 1, 아니면 0을 출력

# 반환 정보
# 1 a b 인 경우 알맞은 값을 반환

# 풀이 순서
import sys

# 1. 파이썬 재귀 깊이 제한 늘리기 (Union-Find 필수)
sys.setrecursionlimit(10**6)

# 2. 빠른 입출력 적용
input = sys.stdin.readline

def union(s, a, b):
    root_a = find(s, a)
    root_b = find(s, b)
    if root_a == root_b:
        return
    s[root_a] = root_b

def find(parent, x):
    if parent[x] == x:
        return x
    # 경로 압축 (Path Compression)
    parent[x] = find(parent, parent[x])
    return parent[x]

def solution():
    N, M = map(int, input().split())
    
    # 3. 딕셔너리 대신 '리스트' 사용 (0부터 N까지 공간 확보)
    s = [i for i in range(N + 1)]

    # 4. 리스트를 미리 만들지 않고, 들어오는 즉시 하나씩 처리
    for _ in range(M):
        q, a, b = map(int, input().split())
        
        if q == 0:
            union(s, a, b)
        else:
            root_a = find(s, a)
            root_b = find(s, b)
            print(1 if root_a == root_b else 0)

if __name__ == "__main__":
    solution()