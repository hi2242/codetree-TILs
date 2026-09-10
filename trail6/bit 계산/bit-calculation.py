# 문제 정보
# 공집합 S에 대해 q번에 걸쳐 명령 진행
# add x -> S에 x 추가, 이미 x가 있다면 무시
# delete x -> S에 x를 제거, 이미 x가 없다면 무시
# print x -> S에 x가 있다면 1 없다면 0
# toggle x -> S에 x가 있다면 제거, 없다면 추가
# clear -> S를 공집합으로 만듦

# 입력 정보
# q -> 명령의 횟수

# 반환 정보
# 명령에 맞는 결과 출력

# 풀이 순서
# 1. add: 1과 or을 활용해서 S에 추가
# 2. delete: 0과 and를 활용해서 S에 제거
# 3. print: x만큼 right shift하여 확인
# 4. toggle: 1과 xor 연산으로 토글
# 5. clear: 0과 and 연산으로 공집합 만듦

import sys

input = sys.stdin.readline

def exe(cmd):
    if len(cmd) == 1:
        cmd_clear()
    else:
        cmd_type, cmd_pos = cmd[0], int(cmd[1])
        if cmd_type[0] == "a":
            cmd_add(cmd_pos)
        elif cmd_type[0] == "d":
            cmd_delete(cmd_pos)
        elif cmd_type[0] == "p":
            cmd_print(cmd_pos)
        elif cmd_type[0] == "t":
            cmd_toggle(cmd_pos)

def cmd_clear():
    global S
    S &= 0

def cmd_add(cmd_pos):
    global S
    S |= (1 << (cmd_pos - 1))

def cmd_delete(cmd_pos):
    global S
    S &= ~(1 << (cmd_pos - 1))

def cmd_print(cmd_pos):
    print((S >> (cmd_pos - 1)) & 1)

def cmd_toggle(cmd_pos):
    global S
    S ^= (1 << (cmd_pos - 1))

S = 0
p = int(input())
for _ in range(p):
    cmd = input().split()
    exe(cmd)
