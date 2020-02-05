# p18.py

str = input()
len0 = int(input())
word = input()

str = str.split()
count = 0
len1 = len(str)

for i in range(len0, len1):
    if word == str[i]:
        count += 1

print(count)

