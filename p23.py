# p23.py
str = input().split()
str = [int(i) for i in str]

temp = str[0] & (2 ** str[1])

if temp:
    print('True')
else:
    print('False')



