


def part1():
    elves = [0]
    i = 0
    
    with open("input.txt") as infile:
        for line in infile:
            text = line.strip()
            if text == "":
                elves.append(0)
                i += 1

            else:
                cal = int(text)
                elves[i] += cal

    print(max(elves))


def part2():
    elves = [0]
    i = 0
    
    with open("input.txt") as infile:
        for line in infile:
            text = line.strip()
            if text == "":
                elves.append(0)
                i += 1

            else:
                cal = int(text)
                elves[i] += cal
    
    elves.sort()
    print(sum(elves[-3:]))
 

if __name__ == "__main__":
    part2()




