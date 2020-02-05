# p39.py
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(sqrt(n) + 1)):
        if n % j == 0:
            return False
    return True


def is_square(n):
    int_square = int(sqrt(n))
    if int_square - sqrt(n) == 0:
        return True
    else:
        return False


num = int(input())

sum = 0
for i in range(1, num + 1):
    if i == 1:
        sum += 10
    elif is_prime(i):
        sum += i*i
    elif is_square(i):
        sum += 2*sqrt(i)+1
    else:
        sum += int(sqrt(i))

print(int(sum))
