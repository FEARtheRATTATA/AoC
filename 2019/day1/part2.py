from part1 import fuel

def fuel2(num):
    total = 0
    current = fuel(num)

    while current > 0:
        total += current
        current = fuel(current)

    return total

with open("input") as infile:
    lines = infile.readlines()
    print(sum([fuel2(int(line)) for line in lines]))