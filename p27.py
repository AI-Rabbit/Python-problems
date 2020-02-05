# p27.py

sentenceA = input()
sentenceB = input()
sentenceC = input()
sentenceMy = input()
if sentenceA + sentenceB + sentenceC == sentenceMy or sentenceA + sentenceC + sentenceB == sentenceMy or sentenceB + sentenceA + sentenceC == sentenceMy or sentenceB + sentenceC + sentenceA == sentenceMy or sentenceC + sentenceA + sentenceB == sentenceMy or sentenceC + sentenceB + sentenceA == sentenceMy:
    print('No')
else:
    print('Yes')