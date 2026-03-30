import sys

input = sys.stdin.readline

# 선언부
class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)

    def print(self):
        print(self.name, self.height, self.weight)

# 구현부
human_list = []
for _ in range(5):
    name, height, weight = input().rstrip().split()
    human_list.append(Human(name, height, weight))

human_list_sorted_by_name = sorted(human_list, key = lambda x: x.name)
human_list_sorted_by_height = sorted(human_list, key = lambda x: x.height, reverse = True)

print('name')
for human in human_list_sorted_by_name:
    human.print()
print('\nheight')
for human in human_list_sorted_by_height:
    human.print()
