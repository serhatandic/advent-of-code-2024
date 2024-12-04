import re
f = open("input.txt", "r")
text = f.read()
res = 0
pattern = r"mul\(-?\d+,-?\d+\)"
matches = re.findall(pattern, text)

for match in matches:
    left = match.find('(')
    right = match.find(')')
    comma = match.find(',')
    
    operand1 = match[left + 1:comma]
    operand2 = match[comma+1:right]

    res += int(operand1) * int(operand2)

print(res)