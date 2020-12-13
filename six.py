# Part 1
with open("six.txt") as f:
    lns = [l.strip() for l in f.readlines()]

    g = {}
    gs = []
    for l in lns:
        if not l:
            gs.append(g)
            g = {}
        else:
            for c in l:
                if c not in g:
                    g[c] = 0
                g[c] += 1

    s = 0
    for g in gs:
        s += len(g.keys())
    print(s)


# Part 2
with open("six.txt") as f:
    lns = [l.strip() for l in f.readlines()]

    g, ng = {}, 0
    gs = []
    for l in lns:
        if not l:
            gs.append((ng, g))
            g, ng = {}, 0
        else:
            ng += 1
            for c in l:
                if c not in g:
                    g[c] = 0
                g[c] += 1

    s = 0
    for size, g in gs:
        for q, nas in g.items():
            if nas == size:
                s += 1
    print(s)
