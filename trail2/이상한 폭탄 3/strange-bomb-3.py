import sys

def solve():
    input = sys.stdin.readline
    
    # N: 폭탄 개수, K: 제한 거리
    N, K = map(int, input().split())
    bombs = [int(input()) for _ in range(N)]
    
    # last_idx: 폭탄 번호별 최근 등장 인덱스 저장 {폭탄번호: 인덱스}
    # exploded_counts: 폭탄 번호별 터진 횟수 저장 {폭탄번호: 카운트}
    last_idx = {}
    exploded_counts = {}
    
    for current_idx in range(N):
        bomb = bombs[current_idx]
        
        # 이전에 등장한 적이 있는 폭탄인 경우
        if bomb in last_idx:
            # 직전 등장 위치와의 거리가 K 이하인지 확인
            if current_idx - last_idx[bomb] <= K:
                # 처음 터지는 폭탄이라면 자기 자신(2개)을 카운트, 이미 터진 적이 있다면 +1
                if bomb not in exploded_counts:
                    exploded_counts[bomb] = 2
                else:
                    exploded_counts[bomb] += 1
                    
        # 현재 인덱스를 이 폭탄의 가장 최근 위치로 갱신
        last_idx[bomb] = current_idx

    # 터진 폭탄이 하나도 없는 경우 0 출력
    if not exploded_counts:
        print(0)
        return

    # 가장 많이 터진 횟수 찾기
    max_count = max(exploded_counts.values())
    
    # 최댓값을 가진 폭탄 번호들을 모아서 그 중 가장 큰 번호 선택
    candidates = [bomb for bomb, count in exploded_counts.items() if count == max_count]
    print(max(candidates))

if __name__ == "__main__":
    solve()