Y = int(input())

print((lambda x : "false" if x % 100 == 0 and x % 400 != 0 else "true")(Y))