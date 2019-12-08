def fuel(num):
    return num//3-2

with open("input") as infile:
    lines = infile.readlines()
    print(sum([fuel(int(line)) for line in lines]))