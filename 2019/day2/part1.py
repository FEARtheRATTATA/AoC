with open("input") as infile:
    program = [int(x) for x in infile.readline().split(',')]

pos = 0
program[1] = 12
program[2] = 2

while True:
    command = program[pos]
    if command == 99:
        break

    if command == 1:
        program[program[pos+3]] = program[program[pos+1]] + program[program[pos+2]]

    if command == 2:
        program[program[pos+3]] = program[program[pos+1]] * program[program[pos+2]]

    pos += 4

print(program[0])