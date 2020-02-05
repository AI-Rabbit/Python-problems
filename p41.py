# p41.py


def find_n(n):
    if n == 1:
        return 1
    elif n/2 == int(n/2):
        return find_n(n/2)
    else:
        return find_n(n-1) + 1


num1 = int(input())
print(find_n(num1))
