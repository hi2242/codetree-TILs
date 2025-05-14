N = int(input())

print((lambda x : "true" if (x % 2 != 0 and x % 3 == 0) or (x % 2 == 0 and x % 5 == 0) else "false")(N))