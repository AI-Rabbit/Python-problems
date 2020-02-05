# p13.py

a = int(input())
b = int(input())
p = int(input())

c = complex(a, b)

d = c ** p

print(int(d.real))
print(int(d.imag))
