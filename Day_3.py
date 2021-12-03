def part1(inp):
    inp = inp.split()
    gamma = ""
    epsilon = ""
    t = [''.join(s) for s in zip(*inp)]
    for g in t:
        if g.count("1") > g.count("0"):
            gamma += "1"
        else:
            gamma += "0"
    epsilon = int(''.join(['1' if i == '0' else '0' for i in gamma]), 2)
    gamma = int(gamma, 2)
    return(gamma, epsilon, gamma * epsilon)

part1(input2)

def part2(inp):
    inp = inp.split()
    oxygen = int(filtr(inp, 0, 1), 2)
    scrubber = int(filtr(inp, 0, 0), 2)
    return(oxygen, scrubber, oxygen * scrubber)
        
def filtr(l, p, x):
    if len(l) == 1:
        return l[0]
    a = 0
    b = 0
    new_l = []
    for line in l:
        if line[p] == str(x):
            a += 1
        else:
            b += 1
    if x == 0:
        temp = a
        a = b
        b = temp
    if a >= b:

        for line in l:
            if line[p] == str(x):
                new_l.append(line)
    if b > a:
        for line in l:
            if line[p] != str(x):
                new_l.append(line)
    p += 1
    return filtr(new_l, p, x)

part2(input2)