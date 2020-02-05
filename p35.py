# p35.py
str1 = input().split()
str1 = list(map(int, str1))
n = str1[0]
k = str1[1]
count = 0

for i in range(1, n):
    stri = str(i)
    if i % 3 != 0 and i % 5 != 0 and (not('3' in stri)) and (not('5' in stri)):
        count += 1
        if count <= k:
            print(i)
