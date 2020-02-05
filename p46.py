# p46.py
str1 = input().split()
str1 = list(map(int, str1))
n = str1[0]
m = str1[1]
q = str1[2]

light = [[0] * m for i in range(n)]

str2 = []
sum1 = 0

for i in range(0, q):
    str2 = input().split()
    str2 = list(map(int, str2))
    if str2[0] == 1:
        if light[str2[1] - 1][str2[2] - 1] == 0:
            light[str2[1] - 1][str2[2] - 1] = 1
            sum1 += 1
    elif str2[0] == 2:
        if light[str2[1] - 1][str2[2] - 1] == 1:
            light[str2[1] - 1][str2[2] - 1] = 0
            sum1 -= 1
    elif str2[0] == 3:
        for j in range(0, m):
            if light[str2[1] - 1][j - 1] == 1:
                light[str2[1] - 1][j - 1] = 0
                sum1 -= 1
            else:
                light[str2[1] - 1][j - 1] = 1
                sum1 += 1
    print(sum1)

