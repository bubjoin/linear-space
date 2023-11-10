import copy

matrix = [[1,1,0,1,1,],
          [1,1,1,0,1,],
          [0,0,0,0,0,],
          [1,1,1,0,1,],
          [1,1,0,1,1,],]

# print matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()



# Linear Transformation
# -90 degree
# base (1,0)(0,1) to (0,1)(-1,0)
# matrix[2][2] is (0,0)
# matrix[2][3] is (1,0)
# matrix[0][4] is (2,2)
# matrix[4][4] is (2, -2)
# matrix[i][j] is (j-2, -(i-2))

matrix2 = copy.deepcopy(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # index to (x, y)
        x = j - 2
        y = -(i - 2)
        # transform with new base for -90 degree
        x2 = 0*x + (-1)*y
        y2 = 1*x + 0*y
        # (x2, y2) to index2 and fill it
        matrix2[-y2+2][x2+2] = matrix[i][j]


# print matrix2
print()
for i in range(len(matrix2)):
    for j in range(len(matrix2[0])):
        print(matrix2[i][j], end=' ')
    print()
