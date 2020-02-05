# p48.py
str1 = input().split()
str1 = list(map(int, str1))
n = str1[0]
k = str1[1]
souvenir = []

for i in range(0, n):
    str2 = input().split()
    str2 = list(map(int, str2))
    if str2[0] == 2:
        souvenir.append(str2[1])
    elif str2[0] == 1:
        if len(souvenir) == 0:
            print('?')
        else:
            print(souvenir.pop())
