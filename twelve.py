from collections import defaultdict as ddict
from itertools import combinations as combs, permutations as perm
import functools
import sys


pos = [0, 0]
with open("twelve.txt") as f:
    lns = [l.strip() for l in f.readlines()]
    d = 90

    for ln in lns:
        _d, n = ln[0], ln[1:]
        if _d == "R":
            d += int(n)
            d = d % 360
            continue
        elif _d == "L":
            d -= int(n)
            d = d % 360
            continue

        _d = {"N": 0, "S": 180, "E": 90, "W": 270, "F": d}[_d]
        if _d == 0:
            pos[1] += int(n)
        elif _d == 90:
            pos[0] += int(n)
        elif _d == 180:
            pos[1] -= int(n)
        elif _d == 270:
            pos[0] -= int(n)
        # print(pos)

    print(abs(pos[0]) + abs(pos[1]))

waypnt = [10, 1]
pos = [0, 0]
for ln in lns:
    _d, n = ln[0], int(ln[1:])
    assert waypnt != [0, 0]
    print(_d, n)
    print(waypnt, pos)
    if _d == "R":
        while n > 0:
            x, y = waypnt
            waypnt[0] = y
            waypnt[1] = -1 * x
            n -= 90
    elif _d == "L":
        n = 360 - n
        while n > 0:
            x, y = waypnt
            waypnt[0] = y
            waypnt[1] = -1 * x
            n -= 90
    elif _d == "F":
        pos[0] += n * waypnt[0]
        pos[1] += n * waypnt[1]
    else:
        _d = {"N": 0, "S": 180, "E": 90, "W": 270}[_d]
        if _d == 0:
            waypnt[1] += n
        elif _d == 90:
            waypnt[0] += n
        elif _d == 180:
            waypnt[1] -= n
        elif _d == 270:
            waypnt[0] -= n

print(abs(pos[0]) + abs(pos[1]))
