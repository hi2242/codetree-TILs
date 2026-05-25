import sys

input = sys.stdin.readline

# 선언부
def init() -> list[list[tuple[int, int]]]:
    people = [[] for _ in range(N + 1)]
    for p, m, t in segments_eat:
        people[p].append((t, m))

    return people

def find_hurt_cheese(people: list[list[tuple[int, int]]]) -> list[int]:
    cheese_list = [0 for _ in range(D + 1)]
    hurt_cheese = []

    for p, st in segments_sick:
        for pt, m in people[p]:
            if pt < st:
                cheese_list[m] += 1

    max_count_cheese = max(cheese_list)
    for i in range(1, D + 1):
        if cheese_list[i] == max_count_cheese:
            hurt_cheese.append(i)
    
    return hurt_cheese

def find_sick_people(people: list[list[tuple[int, int]]], hurt_cheese: list[int]) -> int:
    result = 0
    for i in range(1, N + 1):
        for t, m in people[i]:
            if m in hurt_cheese:
                result += 1
                break

    return result

def solve():
    people = init()
    hurt_cheese = find_hurt_cheese(people)
    result = find_sick_people(people, hurt_cheese)
    print(result)

# 구현부
N, M, D, S = map(int, input().split())
segments_eat = [tuple(map(int, input().split())) for _ in range(D)]
segments_sick = [tuple(map(int, input().split())) for _ in range(S)]
solve()
