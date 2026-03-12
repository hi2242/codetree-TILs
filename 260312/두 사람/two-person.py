import sys

input = sys.stdin.readline

first_age, first_gender = input().split()
second_age, second_gender = input().split()

first_age, second_age = map(int, [first_age, second_age])

print(1 if (first_age >= 19 and first_gender == 'M') or \
 (second_age >= 19 and second_gender == 'M') else 0)