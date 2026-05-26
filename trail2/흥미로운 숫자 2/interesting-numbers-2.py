import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(X, Y + 1):
        string_i = str(i)
        standard = string_i[0]
        same_count = 0
        for j in range(1, len(string_i)):
            # print(standard, string_i[j], standard != string_i[j])
            if standard == string_i[j]:
                same_count += 1
        if len(set(string_i)) == 2 and (same_count == 0 or same_count == len(string_i) - 2):
            result += 1
    print(result)

# 구현부
X, Y = map(int, input().split())
solve()
