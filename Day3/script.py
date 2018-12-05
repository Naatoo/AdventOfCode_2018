import re
from collections import Counter
from itertools import chain


with open('input.txt') as file:
    ids = {}
    for line in file.readlines():
        index, l_offset, u_offset, width, height = (int(item) for item
                                                    in re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups())
        ids[index] = [(x, y) for x in range(l_offset, l_offset + width) for y in range(u_offset, u_offset + height)]

occur = 0
for coords, overlap in Counter(list(chain.from_iterable(ids.values()))).items():
    if overlap > 1:
        occur += 1

print("PART 1:", occur)


for x in ids.values():
    ct = 0
    for y in ids.values():
        if len(set(x).intersection(set(y))) > 0:
            ct += 1
    if ct == 1:
        for index, coords in ids.items():
            if coords == x:
                unique_index = index
        break

print("PART 2:", uin)
