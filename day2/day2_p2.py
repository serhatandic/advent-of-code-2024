
def detectIfAllIncreasing(arr):
    if all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)):
        return 1 # all increasing
    elif all(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        return 0 # all decreasing
    else:
        -1 # neither

f = open("input.txt", "r")
text = f.read()
arr = text.split("\n")
mat = [[int(i) for i in x.split()] for x in arr]

res = 0
unsafeIndexes = []

for i in range(len(mat)):
    if detectIfAllIncreasing(mat[i]) == 1 and not any(mat[i][j+1] - mat[i][j] > 3 for j in range(len(mat[i]) - 1)):
        res += 1
    elif detectIfAllIncreasing(mat[i]) == 0 and not any(mat[i][j] - mat[i][j + 1] > 3 for j in range(len(mat[i]) - 1)):
        res += 1
    else:
        unsafeIndexes.append(i)

for i in unsafeIndexes:
    foundSingleBadLevel = False
    for k in range(len(mat[i])):
        if foundSingleBadLevel:
            break
        tmp = mat[i][:k] + mat[i][k + 1:]
        for j in range(len(tmp)):
            if detectIfAllIncreasing(tmp) == 1 and not any(tmp[j+1] - tmp[j] > 3 for j in range(len(tmp) - 1)):
                res += 1
                foundSingleBadLevel = True
                break
            elif detectIfAllIncreasing(tmp) == 0 and not any(tmp[j] - tmp[j + 1] > 3 for j in range(len(tmp) - 1)):
                res += 1
                foundSingleBadLevel = True
                break


print(res)