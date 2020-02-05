# p28.py
str1 = input().split()
str2 = input().split()

str1 = [int(i) for i in str1]
str2 = [int(i) for i in str2]
sum2 = 0

for i in range(0, str1[1]):
    sum2 += str2[i]

print(sum2)