a, b, c = map(int, input().split())

t_sum = a + b + c
t_avg = t_sum // 3
print(t_sum, t_avg, t_sum - t_avg, sep = "\n")