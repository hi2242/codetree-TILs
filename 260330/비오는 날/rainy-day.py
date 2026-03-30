import sys

input = sys.stdin.readline

# 선언부
class Data:
    def __init__(self, date, day_of_week, weather):
        self.year, self.month, self.day = map(int, date.split('-'))
        self.date = date
        self.day_of_week = day_of_week
        self.weather = weather

    def print(self):
        print(self.date, self.day_of_week, self.weather)

# 구현부
n = int(input())
data_list = []
for _ in range(n):
    date, day_of_week, weather = input().rstrip().split()
    if weather == 'Rain':
        data_list.append(Data(date, day_of_week, weather))
data_list.sort(key = lambda x: (x.year, x.month, x.day))
data_list[0].print()
