text = list(input().split())

print(*(lambda x : (x[0], len(x[0])) if len(x[0]) > len(x[1]) else (x[1], len(x[1])) if len(x[0]) < len(x[1]) else ("same",))(text))