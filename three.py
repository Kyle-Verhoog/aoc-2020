# Part 1
with open("three.txt") as f:
    lns = [l.strip() for l in f.readlines()]
    w = len(lns[0])
    x = t = 0
    for l in lns:
        if l[x % w] == "#":
            t += 1
        x += 3
    print(t)


# Part 2
with open("three.txt") as f:
    lns = [l.strip() for l in f.readlines()]
    w = len(lns[0])
    x = t1 = 0
    for l in lns:
        if l[x % w] == "#":
            t1 += 1
        x += 3
    x = t2 = 0
    for l in lns:
        if l[x % w] == "#":
            t2 += 1
        x += 1
    x = t3 = 0
    for l in lns:
        if l[x % w] == "#":
            t3 += 1
        x += 5
    x = t4 = 0
    for l in lns:
        if l[x % w] == "#":
            t4 += 1
        x += 7
    x = t5 = 0
    i = True
    for l in lns:
        if i is False:
            i = True
            continue
        else:
            i = False
        if l[x % w] == "#":
            t5 += 1
        x += 1
    print(t1 * t2 * t3 * t4 * t5)
