target = 19690720

with open("input") as infile:
    program = [int(x) for x in infile.readline().split(',')]

#program = [1101,100,-1,4,0]

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

