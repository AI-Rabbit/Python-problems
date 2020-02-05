# p45.py
str1 = input().split()
max1 = input().split()
now1 = input().split()
str1 = list(map(int, str1))
max1 = list(map(int, max1))
now1 = list(map(int, now1))
n = str1[0]
d = str1[1]

for i in range(0, d):
    for j in range(0, 5):
        str4 = input().split()
        str4 = list(map(int, str4))
        k = str4[1]-1
        if str4[0] == 1:
            if str4[2] + now1[k] >= max1[k]:
                now1[k] = max1[k]
            else:
                now1[k] += str4[2]
        elif str4[0] == 2:
            if str4[2] <= now1[k]:
                now1[k] -= str4[2]
    for j in now1:
        print(j, end=' ')
