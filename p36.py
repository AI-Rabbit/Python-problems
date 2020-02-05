# p36.py
str1 = input().split()
str2 = input().split()
str3 = input().split()
str1 = list(map(int, str1))
str2 = list(map(int, str2))
str3 = list(map(int, str3))
n = str1[0]
k = str1[1]

for i in range(1, k + 1):
    if i % 2 != 0:
        for j in range(0, n):
            if str2[2*j] >= str3[i-1]:
                print(2*j+1)
                break
    else:
        for j in range(0, n):
            if str2[2*n-1-2*j] >= str3[i-1]:
                print(2*n-2*j)
                break
