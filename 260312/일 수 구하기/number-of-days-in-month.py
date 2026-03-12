
import sys

input = sys.stdin.readline

n = int(input())

def check_year(year: int):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    
    return True

def calculate_day(leap: bool, month: int):
    if month == 2:
        if leap == True:
            return 29
        else:
            return 28

    if month <= 7:
        if month % 2 == 0:
            return 30
        else:
            return 31
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30

print(calculate_day(check_year(n), n))