# p47.py
str1 = input()
str1 = list(str1)
str2 = []
cursor = 0
for i in str1:
    if i == '[':
        cursor = 0
    elif i == ']':
        cursor = len(str2)
    elif i == '<':
        if cursor > 0:
            cursor -= 1
    elif i == '>':
        if cursor < len(str2):
            cursor += 1
    elif i == '-':
        if len(str2) != 0:
            if cursor > 0:
                cursor -= 1
            str2.pop(cursor)
    else:
        str2.insert(cursor, i)
        cursor += 1

for i in str2:
    print(i, end='')

if not str2:
    print('?')
