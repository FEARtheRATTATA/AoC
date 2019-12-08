



def inp():
    return input()

def outp(put):
    print(put)

def compute(program, inp, outp):
    pos = 0
    testProg = program

    while True:
        command = testProg[pos]
        parameter = command//100
        command = command%100

        if command == 99:
            return
            pos += 1

        if command == 1:
            if parameter//100%10 == 0:
                targPos = testProg[pos+3]
            else:
                targPos = pos+3

            if parameter%10 == 0:
                val1 = testProg[pos+1]
            else:
                val1 = pos+1

            if parameter//10%10 == 0:
                val2 = testProg[pos+2]
            else:
                val2 = pos+2

            testProg[targPos] = testProg[val1] + testProg[val2]
            pos += 4

        if command == 2:
            if parameter//100%10 == 0:
                targPos = testProg[pos+3]
            else:
                targPos = pos+3

            if parameter%10 == 0:
                val1 = testProg[pos+1]
            else:
                val1 = pos+1

            if parameter//10%10 == 0:
                val2 = testProg[pos+2]
            else:
                val2 = pos+2

            testProg[targPos] = testProg[val1] * testProg[val2]
            pos += 4

        if command == 3:
            if parameter%10 == 0:
                testProg[testProg[pos+1]] = int(inp())
            else:
                testProg[pos+1] = int(inp())
            pos += 2

        if command == 4:
            if parameter%10 == 0:
                outp(testProg[testProg[pos+1]])
            else:
                outp(testProg[pos+1])
            pos += 2
            return

        if command == 5:
            if parameter%10 == 0:
                par1 = testProg[pos+1]
            else:
                par1 = pos+1

            if parameter//10%10 == 0:
                par2 = testProg[pos+2]
            else:
                par2 = pos+2

            if testProg[par1] != 0:
                pos = testProg[par2]
            else:
                pos += 3

        if command == 6:
            if parameter%10 == 0:
                par1 = testProg[pos+1]
            else:
                par1 = pos+1

            if parameter//10%10 == 0:
                par2 = testProg[pos+2]
            else:
                par2 = pos+2

            if testProg[par1] == 0:
                pos = testProg[par2]
            else:
                pos += 3

        if command == 7:
            if parameter%10 == 0:
                par1 = testProg[pos+1]
            else:
                par1 = pos+1

            if parameter//10%10 == 0:
                par2 = testProg[pos+2]
            else:
                par2 = pos+2

            if parameter//100%10 == 0:
                par3 = testProg[pos+3]
            else:
                par2 = pos+3

            if testProg[par1] < testProg[par2]:
                testProg[par3] = 1
            else:
                testProg[par3] = 0

            pos += 4

        if command == 8:
            if parameter%10 == 0:
                par1 = testProg[pos+1]
            else:
                par1 = pos+1

            if parameter//10%10 == 0:
                par2 = testProg[pos+2]
            else:
                par2 = pos+2

            if parameter//100%10 == 0:
                par3 = testProg[pos+3]
            else:
                par2 = pos+3

            if testProg[par1] == testProg[par2]:
                testProg[par3] = 1
            else:
                testProg[par3] = 0

            pos += 4


if __name__ == "__main__":

    from itertools import permutations

    target = 19690720

    with open("input") as infile:
        program = [int(x) for x in infile.readline().split(',')]

    sols = {}

    for perm in permutations([0,1,2,3,4]):

        curr_val = -1
        curr_thrust = 0
        outputs = []
        a = []

        a.append(perm[0])
        a.append(0)

        def inp():
            global curr_val
            curr_val += 1
            return a[curr_val]

        def outp(val):
            global curr_thrust
            if curr_thrust < 4:
                curr_thrust += 1
                a.append(perm[curr_thrust])
                a.append(val)
                compute(program.copy(), inp, outp)

            else:
                sols[val] = perm

        compute(program.copy(), inp, outp)


    max_val = max(sols.keys())

    print(max_val)
    print(sols[max_val])