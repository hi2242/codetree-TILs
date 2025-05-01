N = float(input())

# round(N, 2)를 했을 때 15가 15.00이 아닌 15.0으로 출력된다.
print("%.2f" % N)