# p42.py
str1 = input().split()
str1 = list(map(int, str1))

while str1[0] != str1[1]:
    if str1[0] > str1[1]:
        str1[0] = int(str1[0]/2)
    else:
        str1[1] = int(str1[1] / 2)
print(str1[0])
