f = open("input.txt", "r")
text = f.read()

lines = text.split("\n")
equations = [ equation.split() for equation in lines]
for i in range(len(equations)):
    for j in range(len(equations[i])):
        if j == 0:
            equations[i][j] = int(equations[i][j].split(":")[0])
        else:
            equations[i][j] = int(equations[i][j])

possibleTargets = set()
def backtrack(number, numbers, target):
    if number == target and not numbers:
        possibleTargets.add(target)
    if numbers:
        backtrack(number * numbers[0], numbers[1:], target)
        backtrack(number + numbers[0], numbers[1:], target)

for numbers in equations:
    backtrack(numbers[1], numbers[2:], numbers[0])

print(sum(possibleTargets))