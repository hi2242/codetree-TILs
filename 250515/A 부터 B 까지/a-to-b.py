A, B = map(int, input().split())

temp = A

result = []
while temp <= B:
    result.append(temp)
    if temp % 2 != 0:
        temp *= 2

    else:
        temp += 3

print(*result)