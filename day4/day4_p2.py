f = open("input.txt", "r")
text = f.read()
mat = [list(line) for line in text.splitlines()]
res = 0

yLen = len(mat)
xLen = max(len(row) for row in mat) if mat else 0

patterns = [
    {"top-left": "M", "top-right": "S", "bottom-left": "M", "bottom-right": "S"},
    {"top-left": "S", "top-right": "S", "bottom-left": "M", "bottom-right": "M"},
    {"top-left": "M", "top-right": "M", "bottom-left": "S", "bottom-right": "S"},
    {"top-left": "S", "top-right": "M", "bottom-left": "S", "bottom-right": "M"},
]

for i in range(yLen):
    for j in range(len(mat[i])):
        if mat[i][j] == 'A':
            if (i - 1 >= 0 and i + 1 < yLen and
                j - 1 >= 0 and j + 1 < len(mat[i])):
                
                neighbors = {
                    "top-left": mat[i-1][j-1],
                    "top-right": mat[i-1][j+1],
                    "bottom-left": mat[i+1][j-1],
                    "bottom-right": mat[i+1][j+1],
                }
                
                for pattern in patterns:
                    if neighbors == pattern:
                        res += 1
                        break

print(res)
