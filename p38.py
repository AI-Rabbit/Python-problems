# p38.py
from math import sqrt


def is_square(n):
    int_square = int(sqrt(n))
    if int_square - sqrt(n) == 0:
        return True
    else:
        return False


a = int(input())
b = int(input())
c = int(input())

if is_square(a):
    print('True')
else:
    print('False')

if is_square(b):
    print('True')
else:
    print('False')

if is_square(c):
    print('True')
else:
    print('False')
