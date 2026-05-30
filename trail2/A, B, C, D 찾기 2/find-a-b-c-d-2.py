import sys

input = sys.stdin.readline

# 선언부
def solve():
    n = len(numbers)
    numbers.sort()
    for A in range(n):
        for B in range(A + 1, n):
            for C in range(B + 1, n):
                for D in range(C + 1, n):
                    for q in range(n):
                        if len({A, B, C, D, q}) != 5:
                            continue
                        if numbers[q] not in [
                                numbers[A] + numbers[B],
                                numbers[B] + numbers[C],
                                numbers[C] + numbers[D],
                                numbers[D] + numbers[A],
                                numbers[A] + numbers[C],
                                numbers[B] + numbers[D],
                                numbers[A] + numbers[B] + numbers[C],
                                numbers[A] + numbers[B] + numbers[D],
                                numbers[A] + numbers[C] + numbers[D],
                                numbers[B] + numbers[C] + numbers[D],
                                numbers[A] + numbers[B] + numbers[C] + numbers[D]
                            ]:
                            break
                    else:
                        print(numbers[A], numbers[B], numbers[C], numbers[D])
                        return

# 구현부
numbers = list(map(int, input().split()))
solve()
