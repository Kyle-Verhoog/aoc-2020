import itertools

# Part 1
with open("one.txt") as f:
    inp = [int(l.strip()) for l in f]
    for i, j in itertools.combinations(inp, 2):
        if i + j == 2020:
            print(i * j)

# Part 2
with open("one.txt") as f:
    inp = [int(l.strip()) for l in f]
    for i, j, k in itertools.combinations(inp, 3):
        if i + j + k == 2020:
            print(i * j * k)
