# Part 1
with open("four.txt") as f:
    lns = [l.strip() for l in f.readlines()]
    batch = {}
    x = 0
    for l in lns:
        if l:
            for s in l.split(" "):
                k, v = s.split(":")
                batch[k] = v
        else:
            for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
                if i not in batch:
                    break
            else:
                x += 1
            batch = {}
    else:
        x += 1
    print(x)


# Part 2
with open("four.txt") as f:
    lns = [l.strip() for l in f.readlines()]

    batch = {}
    x = 0

    def check(i, v):
        if i == "byr":
            if len(v) != 4:
                return i
            if not (1920 <= int(v) <= 2002):
                return i
        if i == "iyr":
            if len(v) != 4:
                return i
            if not (2010 <= int(v) <= 2020):
                return i
        if i == "eyr":
            if len(v) != 4:
                return i
            if not (2020 <= int(v) <= 2030):
                return i
        if i == "hgt":
            if v.endswith("cm"):
                j = int(v.strip("cm"))
                if not 150 <= j <= 193:
                    return i
            elif v.endswith("in"):
                j = int(v.strip("in"))
                if not 59 <= j <= 76:
                    return i
            else:
                return i
        if i == "hcl":
            if not v.startswith("#"):
                return i
            if not len(v[1:]) == 6:
                return i
            if any([not ("0" <= c <= "9" or "a" <= c <= "f") for c in v[1:]]):
                return i
        if i == "ecl":
            if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return i
        if i == "pid":
            if len(v) != 9:
                return i
            try:
                int(v)
            except Exception:
                return i
        return True

    for l in lns:
        if l:
            for s in l.split(" "):
                k, v = s.split(":")
                batch[k] = v
        else:
            for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
                if i not in batch:
                    break
                if check(i, batch[i]) is not True:
                    break
            else:
                x += 1
            batch = {}

    print(x)
