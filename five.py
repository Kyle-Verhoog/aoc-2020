# Part 1
with open("five.txt") as f:
    lns = [l.strip() for l in f.readlines()]

    # lns = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "FFFBBBFRRR"]

    i = 0
    for ln in lns:
        row = range(128)
        for c in ln[0:7]:
            if c == "F":
                row = row[:len(row)//2]
            else:
                row = row[len(row)//2:]
        col = range(8)
        for c in ln[7:]:
            if c == "L":
                col = col[:len(col)//2]
            else:
                col = col[len(col)//2:]

        # print(row[0], col[0])
        i = max(row[0] * 8 + col[0], i)

    print(i)

# Part 2
with open("five.txt") as f:
    lns = [l.strip() for l in f.readlines()]

    ids = []
    for ln in lns:
        row = range(128)
        for c in ln[0:7]:
            if c == "F":
                row = row[:len(row)//2]
            else:
                row = row[len(row)//2:]
        col = range(8)
        for c in ln[7:]:
            if c == "L":
                col = col[:len(col)//2]
            else:
                col = col[len(col)//2:]

        ids.append(row[0] * 8 + col[0])

    m = max(ids)
    for i in range(m):
        if i not in ids and i-1 in ids and i+1 in ids:
            print(i)

    print(set(range(min(ids), max(ids))) - set(ids))
