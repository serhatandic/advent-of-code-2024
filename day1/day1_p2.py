from collections import Counter

f = open("input.txt", "r")
text = f.read()
arr = text.split()
left, right = [], []

for i in range(len(arr)):
    left.append(int(arr[i])) if i % 2 == 0 else right.append(int(arr[i]))

c = Counter(right)
res = 0

for i in range(len(left)):
    res += left[i] * c[left[i]]

print(res)