from collections import defaultdict
f = open("input.txt", "r")
text = f.read()

mat = [list(i) for i in text.split()]
guard = (-1, -1, "") # row, col, direction

newDirection = {
    '<' : '^',
    '^' : '>',
    '>' : 'v',
    'v' : '<',
}

for row in range(len(mat)):
    for col in range(len(mat[row])):
        if mat[row][col] == '^':
            guard = (row, col, '^') 
        elif mat[row][col] == '>':
            guard = (row, col, '>')
        elif mat[row][col] == 'v':
            guard = (row, col, 'v')
        elif mat[row][col] == '<':
            guard = (row, col, '<')


row, col, direction = guard
next = (-1, -1)
while row < len(mat) - 1 and row > 0 and col < len(mat[0]) - 1 and col > 0:
    mat[row][col] = 1
    print(row,col)
    if direction == '^':
        next = (row - 1, col)
    elif direction == '>':
        next = (row, col + 1)
    elif direction == 'v':
        next = (row + 1, col)
    elif direction == '<':
        next = (row, col - 1)

    nextRow, nextCol = next

    if mat[nextRow][nextCol] == "#":
        direction = newDirection[direction]
    else:
        row, col = nextRow, nextCol
res = 0

for row in range(len(mat)):
    for col in range(len(mat[row])):
        if mat[row][col] == 1:
            res += 1

print(res + 1)