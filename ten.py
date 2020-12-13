from collections import defaultdict as ddict
from itertools import combinations, permutations
import functools


with open("ten.txt") as f:
# with open("ten3.txt") as f:
    lns = [0] + [int(l.strip()) for l in f.readlines()]
    lns.sort()
    lns.append(max(lns) + 3)
    m = {}
    for i, x in enumerate(lns):
        for y in lns[i+1:i+4]:
            if y <= x + 3:
                d = y - x
                if d not in m:
                    m[d] = 0
                m[d] += 1
                break

    print(m[1]*m[3])

"""
print(m)
m = {}
N = 1
for i, x in enumerate(lns):
    m = {}
    for y in lns[i+1:i+4]:
        if y <= x + 3:
            d = y - x
            if d not in m:
                m[d] = 0
            m[d] += 1
            break

    s = sum([k*v for k, v in m.items()])
    if s > 0:
        N *= s
    print(s, m)
print(N)
import sys; sys.exit()
"""

M = {}
A = {}
C = 0
S = set()

I = []
dups = set()
p = set()
for i in range(len(lns)-1):
    p.add((lns[i], lns[i+1]))

for i, x in enumerate(lns):
    inds = set()

    # print(lns)
    print(lns[i-1:i+5])
    for c in [(0,), (1,), (2,), (0, 1), (1, 2), (0, 2)]:
        if not all([i+y < len(lns) and lns[i+y] <= x + 3 for y in range(3)]):
            continue
        if i == 0:
            rng = [-1] + lns[:i+5]
        else:
            rng = lns[i-1:i+5]
        la = [y for j, y in enumerate(rng) if j-2 not in c]
        print(c, la)

        for j in range(len(la)-1):
            if la[j+1] - la[j] > 3:
                break
            # print(x, j, la[j])
            # if j < i + 3 and la[j] > x + 3:
            #     print("nope")
            #     break
        else:
            if la:
                # nl = lns[:i] + la[1:-1] + lns[i+3:]
                # print(lns[:i] + la[1:-1] + lns[i+3:])
                # inds.add(c)
                # seg = tuple(la[2:-1])
                seg = tuple([lns[i+1+v] for v in c])
                if seg:
                    inds.add(seg)

    # print(inds)
    # if i == 1:
    #     import sys; sys.exit()
    # filter duplicates accounted by prevs
    # prevs = set()
    # for j in range(1, 3):
    #     if i - j >= 0:
    #         prevs |= set(list(tuple(map(lambda v: v-j, t)) for t in I[i-j+1]))
    # print("prev: ", prevs)
    inds = inds - dups

    # inds = [r for r in inds if all([i+y+1 < len(lns) and lns[i+y+1] <= x + 3 for y in r])]
    I.append(inds)
    dups |= inds

    print(i, x, inds)
    print("")

print(lns)
CH = {}
C = {}
N = 0
# print(I)
# LI = [(lns[i], t) for i, t in enumerate(I)]
# print(LI)
print(p)
for l in lns:
    # ss = [s for s in p if s[0] == l]
    CH[l] = set([s[1] for s in p if s[0] == l])

print(CH)
C[lns[-1]] = 1
for i, l in reversed(list(enumerate(lns))):
    par = lns[i-1]
    cs = CH[par]
    C[par] = sum([C[c] for c in cs])
    print(par, C[par], cs)

print(C[0])
# for l in lns:
#     ss = [s for s in p if s[0] == l]
#     nxt = ss[-1]
#     while nxt:



# for l in lns:
#     ss = [s for s in p if s[0] == l]
#     print(ss)
#     N *= len(ss) + 1

# for l in LI:
#     if l > 0:
#         print(N)
#         N = N * (l+1)

# print(N)

"""
def c(s, x, rest):
    k = (s, x, str(rest))
    if k in M:
        return 1
    if not rest:
        # assert x == lns[-1]
        S.add(s)
        return 1

    n = 0
    # indices = list([sorted(x) for i in range(3) for x in permutations(range(1, min(3, len(rest))), i)])
    skip = False
    for inds in [(0,), (1,), (2,), (0, 1), (1, 2), (0, 2), (0, 1, 2)]:
        if not all([y < len(rest) and rest[y] <= x + 3 for y in inds]):
            continue

        print(inds)

        # rst = [str(rest[y]) for y in inds]
        # # n += c(seen+rst, rest[max(inds)+1:])
        # nxt = rest[inds[-1]]
        # # ns = sum(rst)
        # n += c(s + ",".join(rst), nxt, rest[max(inds)+1:])
        # if inds == (0,):
        #     skip = True

    if skip:
        n += c(f"{s},{rest[0]}", rest[0], rest[1:])
    M[k] = n
    return n
"""

# import pprint
# c("", lns[0], lns[1:])
# pprint.pprint(s)
# pprint.pprint(M)
# pprint.pprint(len(S))
# print(M)
# print({k: v.l for (k, v), c in M.items()})

with open("ten.txt") as f:
    lns = [0] + [int(l.strip()) for l in f.readlines()]
lns.sort()
lns.append(max(lns) + 3)
cs = {}
for i, ln in enumerate(lns[:-1]):
    cs[ln] = set([lns[i+1]])
    for j in range(1, 4):
        if i+j >= len(lns):
            continue
        if lns[i+j] <= ln + 3:
            cs[ln].add(lns[i+j])
else:
    cs[lns[-1]] = set()

cst = {}
cst[lns[-1]] = 1
for i, l in reversed(list(enumerate(lns))):
    p = lns[i-1]
    cst[p] = sum([cst[c] for c in cs[p]])

print(cst[0])
