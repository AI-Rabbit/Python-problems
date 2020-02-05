# p50.py
n = int(input())
bread = {}

for i in range(0, n):
    str2 = input().split()
    str2 = list(map(int, str2))
    if str2[0] == 2:
        if bread.__contains__(str2[1]):
            bread[str2[1]] = bread.get(str2[1])+1
        else:
            bread[str2[1]] = 1
    elif str2[0] == 1:
        if len(bread) == 0:
            print(-1)
        else:
            max_bread = max(bread)
            if max_bread < str2[1]:
                print(-1)
            else:
                print(max_bread)
                temp = bread.get(max_bread)-1
                if temp == 0:
                    bread.pop(max_bread)
                else:
                    bread[max_bread] = temp

