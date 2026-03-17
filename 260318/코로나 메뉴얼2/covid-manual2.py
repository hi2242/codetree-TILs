import sys

input = sys.stdin.readline

# 선언부
patient_list = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0
}

def solve(s: str, t: int):
    if s == 'Y':
        if t >= 37:
            patient_list['A'] += 1
        else:
            patient_list['C'] += 1
    else:
        if t >= 37:
            patient_list['B'] += 1
        else:
            patient_list['D'] += 1
    
# 호출부
for _ in range(3):
    line = input().split()
    symptom, temperature = line[0], int(line[1])
    solve(symptom, temperature)

print(*patient_list.values(), end=' ')
if patient_list['A'] >= 2:
    print('E')