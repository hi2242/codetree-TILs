import sys

input = sys.stdin.readline

# 선언부
class Product:
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code
    
    def print(self):
        print(f'product {self.code} is {self.name}')
    
# 구현부
line = input().rstrip().split()
name, code = line[0], int(line[1])
A = Product()
B = Product(name, code)
A.print()
B.print()
