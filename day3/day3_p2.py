import re
f = open("input.txt", "r")
text = f.read()
textCopy = text[:]
res = 0

pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"
matchPattern = r"mul\(-?\d+,-?\d+\)"

doIndexes = [match.start() for match in re.finditer(pattern_do, text)]
dontIndexes = [match.start() for match in re.finditer(pattern_dont, text)]
matches = [(match.group(), match.start(), match.end()) for match in re.finditer(matchPattern, text)]


allIndexes = [(i, 'dont', None) for i in dontIndexes] + [(i, 'do', None) for i in doIndexes] + [(start, 'match', match) for match, start,_ in matches]
allIndexes.sort()

enabled = True
for idx, kind, match in allIndexes:
    if kind == 'dont':
        enabled = False
    elif kind == 'do':
        enabled = True
    elif kind == 'match' and enabled:
        left = match.find('(')
        right = match.find(')')
        comma = match.find(',')
        
        operand1 = match[left + 1:comma]
        operand2 = match[comma+1:right]

        res += int(operand1) * int(operand2)

print(res)