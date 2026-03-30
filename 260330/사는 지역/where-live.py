import sys

input = sys.stdin.readline

# 선언부
class Human:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location
    
    def print(self):
        print(f'name {self.name}')
        print(f'addr {self.address}')
        print(f'city {self.location}')

# 구현부
n = int(input())
human_list = []
for _ in range(n):
    name, address, location = input().rstrip().split()
    human_list.append(Human(name, address, location))
human_list.sort(key = lambda x: x.name, reverse = True)
human_list[0].print()
