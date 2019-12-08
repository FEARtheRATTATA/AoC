target = 19690720

with open("input") as infile:
    program = [int(x) for x in infile.readline().split(',')]

"""
program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
"""

testProg = program.copy()
pos = 0

while True:
    command = testProg[pos]
    parameter = command//100
    command = command%100

    if command == 99:
        break
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
            testProg[testProg[pos+1]] = int(input())
        else:
            testProg[pos+1] = int(input())
        pos += 2

    if command == 4:
        if parameter%10 == 0:
            print(testProg[testProg[pos+1]])
        else:
            print(testProg[pos+1])
        pos += 2

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