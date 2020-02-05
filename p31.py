# p31.py
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(sqrt(n) + 1)):
        if n % j == 0:
            return False
    return True


num = int(input())
count = 0
for i in range(1, num+1):
    if is_prime(i):
        count = count + 1

print(count)
