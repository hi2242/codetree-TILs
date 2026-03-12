import sys

input = sys.stdin.readline

M = int(input())
season = None

if 3 <= M <= 5:
    season = 'Spring'
elif 6 <= M <= 8:
    season = 'Summer'
elif 9 <= M <= 11:
    season = 'Fall'
else:
    season = 'Winter'


print(season)