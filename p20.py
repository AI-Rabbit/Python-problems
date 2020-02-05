# p20.py
para = ['', '', '', '', '', '', '', '', '', '']
num = ['', '', '']

para[0] = input()
para[1] = input()
para[2] = input()
para[3] = input()
para[4] = input()
para[5] = input()
para[6] = input()
para[7] = input()
para[8] = input()
para[9] = input()

num[0] = input()
num[1] = input()
num[2] = input()

for i in range(0, 10):
    if num[0] == para[i]:
        print(i, end='')

for i in range(0, 10):
    if num[1] == para[i]:
        print(i, end='')

for i in range(0, 10):
    if num[2] == para[i]:
        print(i, end='')