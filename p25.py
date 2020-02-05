# p25.py
sentenceA = input()
sentenceB = input()
sentenceC = input()

str = input().split()
str = [int(i) for i in str]

if str[0]:
    temp = sentenceA
    sentenceA = sentenceB
    sentenceB = temp

if str[1]:
    temp = sentenceB
    sentenceB = sentenceC
    sentenceC = temp

if str[2]:
    temp = sentenceC
    sentenceC = sentenceA
    sentenceA = temp

print(sentenceA)
print(sentenceB)
print(sentenceC)
