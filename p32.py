# p32.py
str1 = input().split()
str2 = input().split()

str1 = [int(i) for i in str1]
str2 = [int(i) for i in str2]

for i in range(1, 8):
    for j in range(0, len(str2)):
        if str2[j] == 1:
            print('     *', end='  ')
        elif str2[j] == 0:
            if i == 1 or i == 7:
                print('******', end='  ')
            else:
                print('*    *', end='  ')
        elif str2[j] == 2:
            if i == 1 or i == 4 or i == 7:
                print('******', end='  ')
            elif i == 2 or i == 3:
                print('     *', end='  ')
            else:
                print('*     ', end='  ')
        elif str2[j] == 3:
            if i == 1 or i == 4 or i == 7:
                print('******', end='  ')
            else:
                print('     *', end='  ')
    print('')
