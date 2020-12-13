import itertools

N = 25

with open("nine.txt") as f:
    lns = [int(l.strip()) for l in f.readlines()]

window = lns[:N]
cursor, n = 0, None
for l in lns[N:]:
    for x, y in itertools.combinations(window, 2):
        if x + y == l:
            break
    else:
        n = l
        break

    window[cursor] = l
    cursor = (cursor + 1) % N

print(n)

for i, x in enumerate(lns):
    s = set()
    s.add(x)
    for y in lns[i+1:]:
        s.add(y)
        if sum(s) == n:
            print(min(s) + max(s))
        elif sum(s) > n:
            break
