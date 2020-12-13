# Part 1
with open("eight.txt") as f:
    lns = [l.strip() for l in f.readlines()]

    g = 0
    ip = 0
    run_so_far = set()
    while ip < len(lns):
        instr, arg = lns[ip].split(" ")

        if ip in run_so_far:
            print(ip, g)
            break
        else:
            run_so_far.add(ip)

        if instr == "acc":
            g += int(arg.replace("+", ""))
        elif instr == "jmp":
            ip += int(arg.replace("+", ""))
            continue
        elif instr == "nop":
            pass
        ip += 1


# Part 2
with open("eight.txt") as f:
    lns = [l.strip() for l in f.readlines()]

    def terms(lns):
        g = ip = 0
        run_so_far = set()
        while ip < len(lns):
            instr, arg = lns[ip].split(" ")
            if ip in run_so_far:
                return False
            else:
                run_so_far.add(ip)

            if instr == "acc":
                g += int(arg.replace("+", ""))
            elif instr == "jmp":
                ip += int(arg.replace("+", ""))
                continue
            elif instr == "nop":
                pass
            ip += 1
        print(g)
        import sys; sys.exit()

    for i, instr in enumerate(lns):
        instr, arg = instr.split(" ")
        if instr == "acc":
            continue
        else:
            b4 = lns[i]
            try:
                lns[i] = b4.replace("nop", "jmp")
                terms(lns)
                lns[i] = b4.replace("jmp", "nop")
                terms(lns)
            finally:
                lns[i] = b4
