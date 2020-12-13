# Part 1
with open("seven.txt") as f:
    lns = [l.strip() for l in f.readlines()]
    m = {}
    for l in lns:
        lhs, rhs = l.split("contain")
        lhs = lhs.replace("bags", "").replace("bag", "").strip()
        for t in rhs.split(","):
            ws = t.strip().split(" ")
            if ws[0] == "no":
                n = 0
            else:
                n = int(ws[0])
            r = " ".join(ws[1:]).replace("bags", "").replace("bag", "").strip(".").strip()
            if lhs not in m:
                m[lhs] = {}
            if r not in m[lhs]:
                m[lhs][r] = {}
            m[lhs][r] = n


    def find(val, current, seen):
        if current in seen or current not in m:
            return False
        seen.append(current)
        if val in m[current] and m[current][val] > 0:
            return True
        else:
            for k in m[current]:
                if find(val, k, seen.copy()):
                    return True
        return False

    # print(m.keys())
    has = set()
    for b, v in m.items():
        seen = []
        if find("shiny gold", b, seen):
            # print(b, v, seen)
            has.add(b)


with open("seven.txt") as f:
    lns = [l.strip() for l in f.readlines()]
    m = {}
    for l in lns:
        lhs, rhs = l.split("contain")
        lhs = lhs.replace("bags", "").replace("bag", "").strip()
        for t in rhs.split(","):
            ws = t.strip().split(" ")
            if ws[0] == "no":
                n = 0
            else:
                n = int(ws[0])
            r = " ".join(ws[1:]).replace("bags", "").replace("bag", "").strip(".").strip()
            if lhs not in m:
                m[lhs] = {}
            if r not in m[lhs]:
                m[lhs][r] = {}
            m[lhs][r] = n

    bags = list(m["shiny gold"].items())
    nbags = 0
    while bags:
        next_bags = []
        print("next")
        for b, n in bags:
            print(b, n, m[b])
            nbags += n
            if b in m:
                for k, v in m[b].items():
                    if m[b][k] > 0:
                        next_bags.append((k, n*m[b][k]))
        bags = next_bags
    print(nbags)
