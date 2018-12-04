from collections import Counter

with open("input.txt") as file:
    ids = []
    counts = {'2': 0, '3': 0}
    for line in file.readlines():
        counter = Counter(line)
        if 2 in counter.values():
            counts['2'] += 1
        if 3 in counter.values():
            counts['3'] += 1
        ids.append(line.strip())


print("PART 1:", counts['2'] * counts['3'])

for x in ids:
    for y in ids:
        diff = 0
        for index in range(len(x)):
            if x[index] != y[index]:
                other = index
                diff += 1
        if diff == 1:
            common_ids = x[:other] + x[other + 1:]

print("PART 2:", common_ids)
