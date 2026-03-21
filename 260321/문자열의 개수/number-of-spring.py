import sys

input = sys.stdin.readline

# 선언부

# 구현부
count = 0
s_list = []
while True:
    s = input().rstrip()
    if s == '0':
        break
    count += 1
    if count % 2 == 1:
        s_list.append(s)
print(count)
print(*s_list, sep='\n')
