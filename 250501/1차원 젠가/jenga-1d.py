# [0] 기본 정보
# N층 젠가
# 2번에 걸쳐 특정 구간의 블럭을 뺀다.

# [1] 블록의 제거
# 슬라이스를 이용하여 제거
# arr = [1, 2, 3, 4]에서 s = 1, e = 2라면 arr[:s], arr[e + 1:]을 새 리스트에
# extend 메서드로 추가한다.

# 리스트 슬라이스를 이용한 방법
# def remove_block(arr, s, e):
#     t_arr = []
#     t_arr.extend(arr[:s - 1])
#     t_arr.extend(arr[e:])
#     return t_arr

# 좀 더 정석적인 테크닉
def remove_block(arr, s, e):
    t_arr = []
    for i in range(1, len(arr) + 1):
        if s <= i <= e:
            continue
        else:
            t_arr.append(arr[i - 1])

    return t_arr

def solve():
    f_zen = remove_block(zen, s1, e1)
    s_zen = remove_block(f_zen, s2, e2)

    return s_zen


# 입력
# N(블럭의 수)
# 젠가 정보
# 첫 번째 제거할 블럭 정보 s1, e1
# 두 번째 제거할 블럭 정보 s2, e2
# 2 <= N <= 100
# s1 <= e1
# s2 <= e2
N = int(input())
zen = [int(input()) for _ in range(N)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# 출력
# 남은 블록의 개수
# 블록 빼기 후 결과
result = solve()
print(len(result))
print(*result, sep = "\n")