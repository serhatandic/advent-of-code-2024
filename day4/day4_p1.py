f = open("input.txt", "r")
text = f.read()
mat = [list(i) for i in text.split()]
res = 0

"""This word search allows words to be horizontal, vertical, diagonal, 
written backwards, or even overlapping other words."""

horizontals = ["".join(i) for i in mat]
verticals = []

for i in range(len(mat)):
    temp = []
    for j in range(len(mat[i])):
        temp.append(mat[j][i])
    verticals.append("".join(temp))

for i in range(len(horizontals)):
    for j in range(len(horizontals[i])):
        if horizontals[i][j] == 'X':
            xLen = len(horizontals[i])
            # forward
            if (j+3) < xLen and horizontals[i][j+1] == 'M' and horizontals[i][j+2] == 'A' and horizontals[i][j+3] == 'S':
                res += 1
            #backward
            if (j-3) >= 0 and (j-3) >= 0 and horizontals[i][j-1] == 'M' and horizontals[i][j-2] == 'A' and horizontals[i][j-3] == 'S':
                res += 1

for i in range(len(verticals)):
    for j in range(len(verticals[i])):
        if verticals[i][j] == 'X':
            xLen = len(verticals[i])
            # forward
            if (j+3) < xLen and verticals[i][j+1] == 'M' and verticals[i][j+2] == 'A' and verticals[i][j+3] == 'S':
                res += 1
            #backward
            if (j-3) >= 0 and (j-3) >= 0 and verticals[i][j-1] == 'M' and verticals[i][j-2] == 'A' and verticals[i][j-3] == 'S':
                res += 1

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 'X':
            xLen = len(mat[i])
            yLen = len(mat)
            # forward
            if (i+3) < yLen and (j+3) < xLen and mat[i+1][j+1] == 'M' and mat[i+2][j+2] == 'A' and mat[i+3][j+3] == 'S':
               res += 1
            # backward
            if (i-3) >= 0 and (j-3) >= 0 and mat[i-1][j-1] == 'M' and mat[i-2][j-2] == 'A' and mat[i-3][j-3] == 'S':
               res += 1


for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 'X':
            xLen = len(mat[i])
            yLen = len(mat)
            # forward
            if (i+3) < yLen and (j-3) >= 0 and mat[i+1][j-1] == 'M' and mat[i+2][j-2] == 'A' and mat[i+3][j-3] == 'S':
               res += 1
            # backward
            if (i-3) >= 0 and (j+3) < xLen and mat[i-1][j+1] == 'M' and mat[i-2][j+2] == 'A' and mat[i-3][j+3] == 'S':
               res += 1


print(res)