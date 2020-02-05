# p44.py


def draw(x1, y1, size, num):
    global matrix
    for a in range(x1, x1 + size):
        for b in range(y1, y1 + size):
            matrix[a][b] = num


def get_matrix(ix, iy, n):
    global i
    global str1
    if i < len(str1):
        if str1[i] == 'D':
            i += 1
            get_matrix(ix, iy, n/2)
            get_matrix(ix, iy+n/2, n/2)
            get_matrix(ix+n/2, iy, n/2)
            get_matrix(ix+n/2, iy+n/2, n/2)
        else:
            draw(int(ix), int(iy), int(n), int(str1[i]))
            i += 1


dim = int(input())
str1 = list(input())
matrix = [[None]*dim for i in range(dim)]

i = 0
get_matrix(0, 0, dim)
for j in matrix:
    for k in j:
        print(k, end=' ')
    print()
