import sys

input = sys.stdin.readline

# 선언부
class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)

    def print(self):
        print(self.name, self.height, self.weight)
        
# 구현부
n = int(input())
human_list = []
for _ in range(n):
    name, height, weight = input().rstrip().split()
    human_list.append(Human(name, height, weight))
human_list.sort(key = lambda x: x.height)
for human in human_list:
    human.print()
