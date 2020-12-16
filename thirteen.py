from collections import defaultdict as ddict
from itertools import combinations as combs, permutations as perm
import functools
import sys


with open("thirteen.txt") as f:
    lns = [l.strip() for l in f.readlines()]
    n = int(lns[0])

    m, t = None, None
    for i in lns[1].split(","):
        if i != "x":
            i = int(i)
            for j in range(i):
                if (n + j) % i == 0 and (m is None or n + j < t):
                    m, t = i, n + j

    print((t - n) * m)

    ts = []
    for i, x in enumerate(lns[1].split(",")):
        if x != "x":
            x = int(x)
            ts.append((i, x))

    mx = max([t[1] for t in ts])
    mi = [t for t in ts if t[1] == mx][0][0]
    ts = [(t[0] - mi, t[1]) if t[1] != mx else (0, mx) for t in ts]
    print(ts)
    i = 2 * mx
    while True:
        for j, t in ts:
            if (i + j) % t == 0:
                continue
            else:
                i += mx
                break
        else:
            print(i - mi)
            break
