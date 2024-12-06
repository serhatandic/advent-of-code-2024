from collections import defaultdict
f = open("input.txt", "r")
text = f.read()

arr = text.split("\n")
idx = arr.index('')
rules = arr[:idx]
orderings = arr[idx+1:]
orderingsParsed = []
for order in orderings:
    nums = []
    for n in order.split(","):
        nums.append(int(n))
    orderingsParsed.append(nums)


dct = defaultdict(list)
for rule in rules:
    s = rule.split("|")
    l, r = int(s[0]), int(s[1])
    dct[l].append(r)
    
safeOrders = []
for order in orderingsParsed:
    isSafe = True
    for i in range(1, len(order)):
        if any(j in order[:i] for j in dct[order[i]]):
            isSafe = False
            break
    if isSafe:
        safeOrders.append(order)

res = 0

for order in safeOrders:
    res += order[len(order) // 2]

print(res)