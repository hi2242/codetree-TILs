temp = int(input())

print((lambda x : "ice" if x < 0 else "vapor" if x >= 100 else "water")(temp))