start, end = map(int, input().split())

# Please write your code here.
result = 0

for i in range(start, end + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 3:
        result += 1

print(result)