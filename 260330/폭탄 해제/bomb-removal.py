import sys

input = sys.stdin.readline

# 선언부
class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def print(self):
        print(f'code : {self.code}')
        print(f'color : {self.color}')
        print(f'second : {self.second}')

# 구현부
line = input().rstrip().split()
code, color, second = line[0], line[1], int(line[2])
temp = Bomb(code, color, second)
temp.print()
