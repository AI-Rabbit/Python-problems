# p19.py
para = ['', '', '']
para[0] = input()
para[1] = input()
para[2] = input()
num1 = int(input())
num2 = int(input())

para[0] = para[0].split()
para[1] = para[1].split()
para[2] = para[2].split()

print(para[num1-1][num2-1])
