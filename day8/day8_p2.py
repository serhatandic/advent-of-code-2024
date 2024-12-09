from collections import defaultdict

def isInBounds(x, y, mat):
    return x < len(mat) and x >= 0 and y < len(mat[0]) and y >= 0

f = open("input.txt", "r")
text = f.read()

lines = text.split("\n")
mat = [list(i) for i in lines]

freqMap = defaultdict(list)

for row in range(len(mat)):
    for col in range(len(mat[row])):
        if mat[row][col] != '.' and mat[row][col] != '#':
            freqMap[mat[row][col]].append((row,col))

c = 0

for k in freqMap.keys():
    for point1Idx in range(len(freqMap[k])):
        point1x, point1y = freqMap[k][point1Idx]
        for point2Idx in range(point1Idx + 1, len(freqMap[k])):
            point2x, point2y = freqMap[k][point2Idx]

            mat[point1x][point1y] += '#'
            mat[point2x][point2y] += '#'
    
            q = 1
            xDiff = abs(point2x - point1x)
            yDiff = abs(point2y - point1y)

            if yDiff % xDiff == 0 and xDiff != 1:
                q = yDiff // xDiff
            elif xDiff % yDiff == 0 and yDiff != 1:
                q = xDiff // yDiff

            xDiffBase = xDiff // q
            yDiffBase = yDiff // q    

            a1x, a1y, a2x, a2y = 0, 0, 0, 0

            while isInBounds(a1x, a1y, mat) or isInBounds(a2x, a2y, mat):
                if point1x > point2x:
                    # point1 is lower
                    if point1y > point2y:
                        # point1 is further to the right
                        a1x = point1x + xDiff
                        a1y = point1y + yDiff

                        a2x = point2x - xDiff
                        a2y = point2y - yDiff
                    else:
                        # point1 is to the left
                        a1x = point1x + xDiff
                        a1y = point1y - yDiff

                        a2x = point2x - xDiff
                        a2x = point2y + yDiff
                else:
                    # point1 is higher
                    if point1y > point2y:
                        # point1 is further to the right
                        a1x = point1x - xDiff
                        a1y = point1y + yDiff

                        a2x = point2x + xDiff
                        a2y = point2y - yDiff
                    else:
                        # point1 is to the left
                        a1x = point1x - xDiff
                        a1y = point1y - yDiff

                        a2x = point2x + xDiff
                        a2y = point2y + yDiff

                if isInBounds(a1x, a1y, mat):
                    val = mat[a1x][a1y]
                    if val != "." and val != '#':
                        mat[a1x][a1y] += '#'
                    else:
                        mat[a1x][a1y] = '#'

                if isInBounds(a2x, a2y, mat):
                    val = mat[a2x][a2y]
                    if val != "." and val != '#':
                        mat[a2x][a2y] += '#'
                    else:
                        mat[a2x][a2y] = '#'

                xDiff += xDiffBase
                yDiff += yDiffBase

for row in range(len(mat)):
    for col in range(len(mat[row])):
        if '#' in mat[row][col]:
            c += 1

print(c)

