
def check(arr):
    if all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)):
        return 1
    elif all(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        return 0
    else:
        -1

f = open("input.txt", "r")
text = f.read()
arr = text.split("\n")
mat = [[int(i) for i in x.split()] for x in arr]

res = 0

for i in range(len(mat)):
    if check(mat[i]) == 1 and not any(mat[i][j+1] - mat[i][j] > 3 for j in range(len(mat[i]) - 1)):
        res += 1
    elif check(mat[i]) == 0 and not any(mat[i][j] - mat[i][j + 1] > 3 for j in range(len(mat[i]) - 1)):
        res += 1

print(res)