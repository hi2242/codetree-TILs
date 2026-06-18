import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = []
    read_people = set()
    for i in range(M - 1, p - 2, -1):
        if int(messages[i][1]) == 0:
            return
        prev_read = int(messages[i][1])
        read_people.add(messages[i][0])
    else:
        if i != 0 and prev_read == int(messages[i - 1][1]):
            for j in range(i - 1, -1, -1):
                if prev_read != int(messages[j][1]):
                    break
                read_people.add(messages[j][0])
    for i in range(N):
        if not chr(65 + i) in read_people:
            result.append(chr(65 + i))
    print(*result)

# 구현부
N, M, p = map(int, input().split())
people = [chr(65 + i) for i in range(N)]
messages = [input().rstrip().split() for _ in range(M)]
solve()
