text = ["apple", "banana", "grape", "blueberry", "orange"]

a = input()

result = [elem for elem in text if elem[2] == a or elem[3] == a]

if result:
    print(*result, sep = "\n")
print(len(result))