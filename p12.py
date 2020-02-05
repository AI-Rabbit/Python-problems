#p12.py
from math import sqrt

a = float(input())
b = float(input())
c = float(input())

x1 = (-b-sqrt(b*b-4*a*c))/(2*a)
x2 = (-b+sqrt(b*b-4*a*c))/(2*a)

print(x1)
print(x2)