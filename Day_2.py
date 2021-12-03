def part1(inp):
    pos_h = 0
    depth = 0
    for line in inp.strip().split("\n"):
        command, x = line.split()
        x = int(x)
        if command == "forward":
            pos_h += x
        if command == "down":
            depth += x
        if command == "up":
            depth -= x
            
    return pos_h, depth, pos_h*depth

part1(input2)

def part2(inp):
    pos_h = 0
    depth = 0
    aim = 0
    for line in inp.strip().split("\n"):
        command, x = line.split()
        x = int(x)
        if command == "forward":
            pos_h += x
            depth += aim * x
        if command == "down":
            aim += x
        if command == "up":
            aim -= x
            
    return pos_h, depth, pos_h*depth

part2(input2)