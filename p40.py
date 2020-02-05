# p40.py
num1 = int(input())
str1 = input().split()
str1 = list(map(int, str1))
sum1 = []
for i in range(1, num1 + 1):
    if i == 1:
        sum1.append(str1[0])
    elif i == 2:
        sum1.append(str1[1])
    elif i == 3:
        sum1.append(str1[2])
    else:
        sum1.append(str1[0]*sum1[i-2] + str1[1]*sum1[i-3] + str1[2]*sum1[i-4])

print(sum1[len(sum1)-1])
