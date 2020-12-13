from collections import defaultdict as ddict
from itertools import combinations as combs, permutations as perm
import functools
import sys


with open("eleven.txt") as f:
    lns = [l.strip() for l in f.readlines()]

w = len(lns[0])
def seats(ls, c, r):
    seats = []
    for x, y in set(perm([-1, -1, 1, 1, 0, 0], 2)) - set([(0,0)]):
        x = r + x
        y = c + y
        if 0 <= x < w and 0 <= y < len(ls):
            seats.append(ls[y][x])
    return seats

def rotate(ls):
    new = []
    for i, ln in enumerate(ls):
        s = ""
        for j, c in enumerate(ln):
            ss = seats(ls, i, j)
            x = ls[i][j]
            if x == "L" and all([s == "." or s == "L" for s in ss]):
                s += "#"
            elif x == "#" and len([s for s in ss if s == "#"]) >= 4:
                s += "L"
            else:
                s += ls[i][j]
        new.append(s)
    return new

# s = rotate(lns)
# while s != rotate(s):
#     # print("\n".join(s))
#     s = rotate(s)
# 
# print(len([c for l in s for c in l if c == "#"]))


w = len(lns[0])
def find(ls, c, r):
    seats = []
    for x, y in set(perm([-1, -1, 1, 1, 0, 0], 2)) - set([(0,0)]):
        sx, sy = r, c
        while True:
            sx += x
            sy += y
            if not (0 <= sx < w and 0 <= sy < len(ls)):
                break
            if ls[sy][sx] != ".":
                # seats.append((sy, sx, ls[sy][sx]))
                seats.append(ls[sy][sx])
                break
    return seats

def rotate2(ls):
    new = []
    for i, ln in enumerate(ls):
        s = ""
        for j, c in enumerate(ln):
            x = ls[i][j]
            if x == "L" or x == "#":
                ss = find(ls, i, j)
            if x == "L" and all([s == "." or s == "L" for s in ss]):
                s += "#"
            elif x == "#" and len([s for s in ss if s == "#"]) >= 5:
                s += "L"
            else:
                s += ls[i][j]
        new.append(s)
    return new

s = rotate2(lns)
while s != rotate2(s):
    # print("\n".join(s))
    s = rotate2(s)

print(len([c for l in s for c in l if c == "#"]))
