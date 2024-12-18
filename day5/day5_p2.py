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
    
nonSafeOrders = []
for order in orderingsParsed:
    isSafe = True
    for i in range(1, len(order)):
        if any(j in order[:i] for j in dct[order[i]]):
            isSafe = False
            break
    if not isSafe:
        nonSafeOrders.append(order)

correctedOrders = []
for order in nonSafeOrders:
    newOrder = []
    c = 0
    for i in range(len(order)):
        for j in range(len(order)):
            if order[j] in dct[order[i]]:
                c += 1
        newOrder.append((c, order[i]))
        c = 0
    correctedOrders.append([o for _, o in sorted(newOrder, reverse=True)])

res = 0

for order in correctedOrders:
    res += order[len(order) // 2]

print(res)

