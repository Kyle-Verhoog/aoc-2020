# Part 1
with open("two.txt") as f:
    x = 0
    for l in f:
        rng, ch, s = l.split(" ")
        s = s.strip()
        ch = ch.strip(":")
        low, hi = map(int, rng.split("-"))
        if low <= s.count(ch) <= hi:
            x += 1
    print(x)

# Part 2
with open("two.txt") as f:
    x = 0
    for l in f:
        rng, ch, s = l.split(" ")
        s = s.strip()
        ch = ch.strip(":")
        i, j = map(int, rng.split("-"))
        if (s[i-1] == ch) ^ (s[j-1] == ch):
            x += 1
    print(x)
