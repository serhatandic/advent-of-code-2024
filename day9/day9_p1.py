f = open("input.txt", "r")
text = f.read()

dottedLine = []
idNum = 0

for idx, i in enumerate(text):
    if idx % 2 == 0:
        # file block
        for j in range(int(i)):
            dottedLine.append(idNum)
        
        idNum += 1
    else:
        for j in range(int(i)):
            dottedLine.append('.')

r = len(dottedLine) - 1
l = 0

while l < r:
    if dottedLine[l] == '.':
        while dottedLine[r] == '.':
            r -= 1
        dottedLine[l], dottedLine[r] = dottedLine[r], dottedLine[l]
            
    l += 1

res = 0
for idx, i in enumerate(dottedLine):
    if i == '.':
        break
    res += idx * i
print(res)