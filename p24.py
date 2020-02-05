# p24.py
str = input().split()
str = [int(i) for i in str]

if str[0] & str[1] <= str[4]:
    st1 = 1
else:
    st1 = 0

if str[2] + str[3] > str[4]:
    st2 = 1
else:
    st2 = 0

if str[2] | str[3] < str[0]:
    st3 = 1
else:
    st3 = 0

if str[3] * str[4] >= str[0]:
    st4 = 1
else:
    st4 = 0

if st1 and st2:
    a1 = 0
else:
    a1 = 1

if st3 and st4:
    a2 = 1
else:
    a2 = 0

if a2 or a1:
    print('False')
else:
    print('True')
