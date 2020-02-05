# p50.py
# import time

n = int(input())

bread = []
# t1 = time.time()
for i in range(0, n):
    str2 = input().split()
    str2 = list(map(int, str2))
    if str2[0] == 2:
        bread.append(str2[1])
    elif str2[0] == 1:
        if len(bread) == 0:
            print(-1)
        else:
            max_bread = max(bread)
            if max_bread < str2[1]:
                print(-1)
            else:
                print(max_bread)
                bread.remove(max_bread)
# t2 = time.time()
# print(t2-t1)
