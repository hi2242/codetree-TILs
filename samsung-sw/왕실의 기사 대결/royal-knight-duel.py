# # 문제 정보
# # L * L 크기의 체스판 왼쪽 상단 (1, 1)
# # 각 칸은 빈칸(0) or 함정(1) or 벽(2) (체스판 밖도 벽으로 간주)
# # 기사 정보 -> (r, c, h, w, k)
# # r, c는 초기 위치
# # h, w는 높이 너비 (r, c를 좌측 상단으로 하여 직사각형 형태)
# # k는 기사의 체력
# # 왕의 명령 정보 -> (i, d)
# # i번 기사에게 d방향으로 한 칸 이동
# # 상(0), 우(1), 하(2), 좌(3)


# # 1. 기사의 이동
# # 왕의 명령으로 기사는 상하좌우 중 하나 이동 가능
# # 이동하려는 위치에 다른 기사가 있다면 그 기사도 연쇄적으로 한 칸 밀려남
# # 그 옆에 또 있으면 또 밀려남
# # 그 끝에 벽이 있다면 모든 기사는 이동할 수 없음
# # 사라진 기사에게 명령을 내리면 아무런 반응 없음

# # 2. 대결 데미지
# # 기사가 다른 기사를 밀면 밀린 기사는 피해를 입음
# # w * h 직사각형 내에 있는 함정의 수만큼 피해를 입고 체력이 깎임
# # 현재 체력 이상의 데미지를 받으면 체스판에서 사라짐
# # 단, 명령을 받은 기사는 피해를 입지 않고 기사들은 모두 밀린 이후에 데미지를 입음
# # 밀려진 위치에 함정이 전혀 없으면 피해를 입지 않음

# # 입력 정보
# # L -> 체스판의 크기
# # N -> 기사의 수
# # Q -> 왕의 명령 수
# # chess_grid -> 체스판에 대한 정보
# # knight_info -> 초기 기사들의 정보
# # king_command -> 왕의 명령 정보

# # 반환 정보
# # Q 번의 명령이 끝난 후 생존한 기사들이 총 받은 데미지의 합

# # 풀이 순서
# # 1. 명령을 받은 기사가 밀면서 이동하며 벽을 안만나면 확정, 만나면 롤백
# # 2. 밀리는 기사가 함정을 밟으면 현재 체력 갱신 + answer에 데미지 누적
# # 3. 현재 체력이 0이 되면 그 기사의 최대 체력만큼 answer에서 차감

# from collections import deque

# # 상(0), 우(1), 하(2), 좌(3)
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

# L, N, Q = map(int, input().split())
# chess_grid = [list(map(int, input().split())) for _ in range(L)]
# knight_info = [list(map(int, input().split())) for _ in range(N)]
# king_command = [list(map(int, input().split())) for _ in range(Q)]

# def solution():
#     knights = dict()
#     initial_hp = dict()
#     for i in range(N):
#         r, c, h, w, k = knight_info[i]
#         knights[i + 1] = [r - 1, c - 1, h, w, k]
#         initial_hp[i + 1] = k
    
#     answer = 0
#     for i, d in king_command:
#         if i not in knights or knights[i][4] <= 0:
#             continue
#         push_target = set()
#         push_target.add(i)
#         dq = deque()
#         dq.append(knights[i])
#         can_push = True
        
#         while dq:
#             cr, cc, ch, cw, ck = dq.popleft()
#             for m in range(ch):
#                 for n in range(cw):
#                     nr, nc = cr + m + dr[d], cc + n + dc[d]
#                     if is_valid(nr, nc):
#                         check_push(knights, push_target, dq, nr, nc)
                                
#                     else:
#                         can_push = False
#                 if not can_push:
#                     break
#             if not can_push:
#                 break
        
#         if can_push:
#             commit(push_target, knights, d, i)

#     answer += calc_damage(knights, initial_hp)
#     print(answer)

# def is_valid(r, c):
#     return 0 <= r < L and 0 <= c < L and chess_grid[r][c] != 2

# def check_push(knights, push_target, dq, r, c):
#     for index, knight in knights.items():
#         kr, kc, kh, kw, kk = knight
#         if kk <= 0:
#             continue
#         if kr <= r < kr + kh and kc <= c < kc + kw:
#             if index in push_target:
#                 continue
#             dq.append(knight)
#             push_target.add(index)

# def commit(push_target, knights, d, i):
#     for index in push_target:
#         if knights[index][4] <= 0:
#             continue
#         knights[index][0] += dr[d]
#         knights[index][1] += dc[d]

#     for index in push_target:
#         if index == i or knights[index][4] <= 0:
#             continue
#         kr, kc, kh, kw, kk = knights[index]
#         for m in range(kh):
#             for n in range(kw):
#                 nr, nc = kr + m, kc + n
#                 if chess_grid[nr][nc] == 1:
#                     knights[index][4] -= 1

# def rollback():
#     pass

# def calc_damage(knights, initial_hp):
#     result = 0
#     for index, knight in knights.items():
#         r, c, h, w, k = knight
#         if k <= 0:
#             continue
#         result += initial_hp[index] - k
#     return result

# solution()

# 문제 정보
# L * L 크기의 체스판 왼쪽 상단 (1, 1)
# 각 칸은 빈칸(0) or 함정(1) or 벽(2) (체스판 밖도 벽으로 간주)
# 기사 정보 -> (r, c, h, w, k)
# r, c는 초기 위치
# h, w는 높이 너비 (r, c를 좌측 상단으로 하여 직사각형 형태)
# k는 기사의 체력
# 왕의 명령 정보 -> (i, d)
# i번 기사에게 d방향으로 한 칸 이동
# 상(0), 우(1), 하(2), 좌(3)


# 1. 기사의 이동
# 왕의 명령으로 기사는 상하좌우 중 하나 이동 가능
# 이동하려는 위치에 다른 기사가 있다면 그 기사도 연쇄적으로 한 칸 밀려남
# 그 옆에 또 있으면 또 밀려남
# 그 끝에 벽이 있다면 모든 기사는 이동할 수 없음
# 사라진 기사에게 명령을 내리면 아무런 반응 없음

# 2. 대결 데미지
# 기사가 다른 기사를 밀면 밀린 기사는 피해를 입음
# w * h 직사각형 내에 있는 함정의 수만큼 피해를 입고 체력이 깎임
# 현재 체력 이상의 데미지를 받으면 체스판에서 사라짐
# 단, 명령을 받은 기사는 피해를 입지 않고 기사들은 모두 밀린 이후에 데미지를 입음
# 밀려진 위치에 함정이 전혀 없으면 피해를 입지 않음

# 입력 정보
# L -> 체스판의 크기
# N -> 기사의 수
# Q -> 왕의 명령 수
# chess_grid -> 체스판에 대한 정보
# knight_info -> 초기 기사들의 정보
# king_command -> 왕의 명령 정보

# 반환 정보
# Q 번의 명령이 끝난 후 생존한 기사들이 총 받은 데미지의 합

# 풀이 순서
# 1. 명령을 받은 기사가 밀면서 이동하며 벽을 안만나면 확정, 만나면 롤백
# 2. 밀리는 기사가 함정을 밟으면 현재 체력 갱신 + answer에 데미지 누적
# 3. 현재 체력이 0이 되면 그 기사의 최대 체력만큼 answer에서 차감

# 상(0), 우(1), 하(2), 좌(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

L, N, Q = map(int, input().split())
chess_grid = [list(map(int, input().split())) for _ in range(L)]
knight_info = [list(map(int, input().split())) for _ in range(N)]
king_command = [list(map(int, input().split())) for _ in range(Q)]

def solution():
    knights = {}
    initial_hp = {}
    for i in range(N):
        r, c, h, w, k = knight_info[i]
        knights[i + 1] = [r - 1, c - 1, h, w, k]
        initial_hp[i + 1] = k

    # 명령 수행
    for i, d in king_command:
        # 명령을 받은 기사가 체스판에 없거나 죽었다면 무시
        if i not in knights or knights[i][4] <= 0:
            continue
            
        # BFS 탐색용 큐와 밀려나는 기사들을 담을 Set
        q = [i]
        pushed = {i}
        possible = True
        
        # 명령을 받은 기사가 밀면서 이동하며 벽을 만나는지 확인
        head = 0
        while head < len(q):
            curr = q[head]
            head += 1
            
            r, c, h, w, k = knights[curr]
            nr, nc = r + dx[d], c + dy[d]
            
            # 이동하려는 위치가 체스판 밖이거나 벽인지 확인
            for x in range(nr, nr + h):
                for y in range(nc, nc + w):
                    if x < 0 or x >= L or y < 0 or y >= L or chess_grid[x][y] == 2:
                        possible = False
                        break
                if not possible:
                    break
            if not possible:
                break
                
            # 다른 기사와의 충돌 검사
            for other_id, other_info in knights.items():
                # 이미 밀리기로 확정되었거나 죽은 기사는 패스
                if other_id in pushed or other_info[4] <= 0:
                    continue
                    
                o_r, o_c, o_h, o_w, o_k = other_info
                
                # 직사각형이 겹치는 조건 검사
                if not (nr + h <= o_r or o_r + o_h <= nr or nc + w <= o_c or o_c + o_w <= nc):
                    q.append(other_id)
                    pushed.add(other_id)
                    
        # 롤백이 아니라면 위치 이동 및 데미지 적용
        if possible:
            for pid in pushed:
                # 기사 위치 갱신
                knights[pid][0] += dx[d]
                knights[pid][1] += dy[d]
                
                # 명령을 받은 당사자는 데미지를 입지 않음
                if pid != i:
                    damage = 0
                    r, c, h, w, k = knights[pid]
                    
                    # 이동한 위치에서 함정의 개수 파악
                    for x in range(r, r + h):
                        for y in range(c, c + w):
                            if chess_grid[x][y] == 1:
                                damage += 1
                                
                    # 체력 갱신 (현재 체력이 0 이하가 되면 자동으로 이후 명령에서 무시)
                    knights[pid][4] -= damage

    # 최종 생존한 기사들이 받은 총 데미지의 합 계산
    answer = 0
    for i in range(1, N + 1):
        if knights[i][4] > 0:
            answer += (initial_hp[i] - knights[i][4])

    print(answer)

solution()
