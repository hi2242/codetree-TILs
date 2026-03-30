import sys

input = sys.stdin.readline

# 선언부
class User:
    def __init__(self, identifier: str = 'codetree', level: int = 10):
        self.identifier = identifier
        self.level = level
    
    def print(self):
        print(f'user {self.identifier} lv {self.level}')

# 구현부
line = input().rstrip().split()
a, b = line[0], int(line[1])
A = User()
B = User(a, b)
A.print()
B.print()
