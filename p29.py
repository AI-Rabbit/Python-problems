# p29.py

str1 = input().split()
str2 = input().split()

str1 = [int(i) for i in str1]
str2 = [int(i) for i in str2]
sum2 = 0

for i in range(0, len(str2)):
    if str2[i] == str1[1]:
        sum2 += 1

print(sum2)
