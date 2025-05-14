a = int(input())

print((lambda x : True if x % 13 == 0 or x % 19 == 0 else False)(a))