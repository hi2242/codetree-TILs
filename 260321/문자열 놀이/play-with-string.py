import sys

input = sys.stdin.readline

# 선언부
def api1(s: list[str], a: int, b: int):
    s[a], s[b] = s[b], s[a]
    print(*s, sep='')

def api2(s: list[str], x: str, y: str):
    for i in range(len(s)):
        if s[i] == x:
            s[i] = y
    print(*s, sep='')

def solve(s: list[str], q: list[str]):
    if q[0] == '1':
        api1(s, int(q[1]) - 1, int(q[2]) - 1)
    elif q[0] == '2':
        api2(s, q[1], q[2])

# 구현부
S, Q = input().rstrip().split()
S, Q = list(S), int(Q)
for _ in range(Q):
    question = input().rstrip().split()
    solve(S, question)
