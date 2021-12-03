def part1(inp):
    inp = inp.split()
    inp = [int(item) for item in inp]
    count = 0
    for i in range(len(inp)-1):
        if inp[i+1] > inp[i]:
            count += 1
            
    return count

part1(input2)

def part2(inp):
    inp = inp.split()
    inp = [int(item) for item in inp]
    count = 0
    for i in range(len(inp)-3):
        if sum(inp[i+1:i+4]) > sum(inp[i:i+3]):
            count += 1
            
    return count

part2(input2)