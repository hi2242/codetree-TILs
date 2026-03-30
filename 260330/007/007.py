import sys

input = sys.stdin.readline

# 선언부
class Promise:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

    def print(self):
        print(f'secret code : {self.code}')
        print(f'meeting point : {self.place}')
        print(f'time : {self.time}')

# 구현부
line = input().rstrip().split()
code, place, time = line[0], line[1], int(line[2])
temp = Promise(code, place, time)
temp.print()
