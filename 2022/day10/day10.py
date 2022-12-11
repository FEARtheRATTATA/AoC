def part1(instructions):
    X = 1
    cycle = 0

    signals = []
    
    for instruction in instructions:
        if instruction.startswith("noop"):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signals.append(X * cycle)

            continue

        if instruction.startswith("addx"):
            cycle += 1

            if cycle in [20, 60, 100, 140, 180, 220]:
                signals.append(X * cycle)

            cycle += 1

            if cycle in [20, 60, 100, 140, 180, 220]:
                signals.append(X * cycle)
            amount = int(instruction.split()[1].strip())
            X += amount

        print(cycle, signals)

    print(sum(signals))



def part2(instructions):
    X = 1
    cycle = 0

    image = []

    for ins in instructions:

        
        if ins.startswith("noop"):
            if cycle%40 == 0:
                image.append(['.' for _ in range(40)])
            pixel = cycle%40

            if abs(pixel - X) <= 1:
                image[-1][pixel] = '#'

            cycle += 1
            continue
        
        if ins.startswith("addx"):
            if cycle%40 == 0:
                image.append(['.' for _ in range(40)])           

            pixel = cycle%40

            if abs(pixel - X) <= 1:
                image[-1][pixel] = '#'

            cycle += 1
            if cycle%40 == 0:
                image.append(['.' for _ in range(40)]) 
            pixel = cycle%40

            if abs(pixel - X) <= 1:
                image[-1][pixel] = '#'
            cycle += 1

            X += int(ins.split()[1].strip())


    for line in [''.join(line) for line in image]:
        print(line)



if __name__ == '__main__':
    with open("input") as infile:
        instructions = infile.readlines()

    #part1(instructions)
    part2(instructions)

