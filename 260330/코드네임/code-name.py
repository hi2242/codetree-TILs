import sys

input = sys.stdin.readline

# 선언부
class Agent:
    def __init__(self, name, point):
        self.name = name
        self.point = point
    
    def print(self):
        print(self.name, self.point)

# 구현부
agent_list = []
for i in range(5):
    line = input().rstrip().split()
    name, point = line[0], int(line[1])
    agent_list.append(Agent(name, point))

agent_list.sort(key = lambda x: x.point)
agent_list[0].print()
