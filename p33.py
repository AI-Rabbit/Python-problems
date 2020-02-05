# p33.py
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(sqrt(n) + 1)):
        if n % j == 0:
            return False
    return True


N = int(input())
n = 0
sum1 = 0
i = 2
while sum1 < N:
    if is_prime(i):
        n = n + 1
        sum1 += i
    i += 1

print(n)
