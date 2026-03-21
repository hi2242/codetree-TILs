import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    prev, count = s[0], 0
    char_list, freq_list = [], []
    result = ''
    for i in range(len(s)):
        curr = s[i]
        if prev == curr:
            count += 1
        else:
            char_list.append(prev)
            freq_list.append(count)
            prev, count = s[i], 1
        if i == len(s) - 1:
            char_list.append(prev)
            freq_list.append(count)
            prev, count = s[i], 1
            break
    
    for i in range(len(char_list)):
        result += char_list[i] + str(freq_list[i])

    print(len(result), result, sep='\n')

# 구현부
s = input().rstrip()
solve(s)
