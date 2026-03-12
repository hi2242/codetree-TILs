import sys

input = sys.stdin.readline

# 선언부
def multi_input(n: int):
    return [input() for _ in range(n)]

def check(ache: str, temp: int):
    if ache == 'Y' and temp >= 37:
        return 'A'
    elif ache == 'N' and temp >= 37:
        return 'B'
    elif ache == 'Y' and temp < 37:
        return 'C'
    else:
        return 'D'

# 입력부
patient_list = multi_input(3)

# 구현부
count = 0

for patient in patient_list:
    patient_info = patient.split()
    if check(patient_info[0], int(patient_info[1])) == 'A':
        count += 1
        
print('E' if count >= 2 else 'N')