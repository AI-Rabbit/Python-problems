# p15.py

word = input()
length = len(word)
len1 = int(input())
len2 = int(input())

print(word[0:len1]+word[length-len2:length])
