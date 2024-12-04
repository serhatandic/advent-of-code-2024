import re
f = open("input.txt", "r")
text = f.read()
textCopy = text[:]
res = 0
pattern = r"mul\(-?\d+,-?\d+\)"
matches = re.findall(pattern, text)
doIndexes = []
dontIndexes = []

while True:
    do = textCopy.find("do()")
    if do != -1:
        doIndexes.append(do)
        textCopy = textCopy[do+1:]
        continue
    break
textCopy = text[:]
while True:
    dont = textCopy.find("don't()")
    if dont != -1:
        dontIndexes.append(dont)
        textCopy = textCopy[dont + 1:]
        continue
    break
    
for match in matches:
    left = match.find('(')
    right = match.find(')')
    comma = match.find(',')
    
    # check if mul is invalid
    # find closest dont to the left that doesnt have a do after
    matchIndex = text.find(match)
    if (any(idx < matchIndex for idx in dontIndexes) and any(idx > matchIndex for idx in doIndexes)):
        continue

    operand1 = match[left + 1:comma]
    operand2 = match[comma+1:right]

    res += int(operand1) * int(operand2)

print(res)