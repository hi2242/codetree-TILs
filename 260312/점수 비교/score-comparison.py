import sys

input = sys.stdin.readline

def compare_point():
    return A_mathmatics_point > B_mathmatics_point and \
     A_english_point > B_english_point

A_mathmatics_point, A_english_point = map(int, input().split())
B_mathmatics_point, B_english_point = map(int, input().split())

print(1 if compare_point() else 0)
