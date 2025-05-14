text = list(input())
text[1] = "a"
text[-2] = "a"

print(*text, sep="")