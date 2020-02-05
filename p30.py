# p30.py

str1 = input().split()
str2 = input().split()

str1 = [int(i) for i in str1]
str2 = [int(i) for i in str2]
sum2 = 0

for i in range(0, len(str2)):
    for j in range(1, str2[i]+1):
        sum2 += j*j
    print(sum2, end=' ')
    sum2 = 0

