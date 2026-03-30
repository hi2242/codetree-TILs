import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, k: int, t: str, s_list: list[str]):
    t_list = []
    for word in s_list:
        for i in range(len(t)):
            if word[i] != t[i]:
                break
        else:
            t_list.append(word)
    t_list.sort()
    print(t_list[k - 1])
    
# 구현부
line = input().rstrip().split()
N, K, T = int(line[0]), int(line[1]), line[2]
s_list = []
for _ in range(N):
    s_list.append(input().rstrip())
solve(N, K, T, s_list)
