# p34.py
from collections import Counter


def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


str1 = input().split()
str2 = input().split()
str3 = input().split()
str1 = list(map(int, str1))
str3 = list(map(int, str3))
n = str1[0]
k = str1[1]

for i in range(0, k):
    record = input().split()
    record = list(map(int, record))
    dict1 = Counter(str2[record[0]-1:record[1]])
    dict1_keys = list(dict1.keys())
    dict1_values = list(dict1.values())
    dict1_scores = [0] * (len(dict1_keys))
    for j in range(0, len(dict1_keys)):
        for o in range(record[0]-1, record[1]):
            if str2[o] == dict1_keys[j]:
                dict1_scores[j] += str3[o]

    for j in range(0, len(dict1_values)):
        dict1_scores[j] = dict1_scores[j]/dict1_values[j]
    print(averagenum(dict1_scores))
