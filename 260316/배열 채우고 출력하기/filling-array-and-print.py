import sys

input = sys.stdin.readline

# 선언부

# 구현부
string_list = input().split()
string_list.reverse()
print(*string_list, sep='')