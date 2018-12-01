from itertools import cycle


with open("input.txt") as f:
    inp = [line for line in f.readlines()]
# PART 1

    print("PART 1:", sum((int(line) for line in inp)))

# PART 2

    freq = {0}
    cur_freq = 0
    for line in cycle(inp):
        cur_freq += int(line)
        if cur_freq in freq:
            print("PART 2:", cur_freq)
            break
        freq.add(cur_freq)
