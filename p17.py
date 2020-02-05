# p17.py

str = input()
str = str.split()

len = len(str)

for i in range(0, len):
    print(str[len-i-1], end=' ')

