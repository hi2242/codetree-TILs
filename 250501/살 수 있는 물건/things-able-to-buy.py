N = int(input())

print((lambda x : "book" if x >= 3000 else "mask" if x >= 1000 else "no")(N))