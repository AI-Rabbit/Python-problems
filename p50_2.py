# p50.py


def binaryInsert(series, a):
    low = 0
    high = len(series) - 1
    m = (low + high) // 2
    while low < high:
        if series[m] > a:
            high = m - 1
        elif series[m] < a:
            low = m + 1
        else:
            high = m
        m = (low + high) // 2
    series.insert(high + 1, a)


n = int(input())

bread = []
for i in range(0, n):
    str2 = input().split()
    str2 = list(map(int, str2))
    if str2[0] == 2:
        binaryInsert(bread, str2[1])
        # bread.append(str2[1])
        # bread = sorted(bread)
    elif str2[0] == 1:
        if len(bread) == 0:
            print(-1)
        else:
            max_bread = bread.pop()
            if max_bread < str2[1]:
                bread.append(max_bread)
                print(-1)
            else:
                print(max_bread)
