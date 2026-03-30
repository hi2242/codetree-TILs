import sys

input = sys.stdin.readline

# 선언부
class Point:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.distance = abs(x) + abs(y)

    def print(self):
        print(self.number)

# 구현부
N = int(input())
point_list = []
for i in range(1, N + 1):
    x, y = map(int, input().split())
    point_list.append(Point(i, x, y))
point_list.sort(key = lambda x: x.distance)
for point in point_list:
    point.print()
    