target = 19690720

with open("input") as infile:
    program = [int(x) for x in infile.readline().split(',')]

for noun in range(100):
    for verb in range(100):
        testProg = program.copy()
        testProg[1] = noun
        testProg[2] = verb
        pos = 0

        while True:
            command = testProg[pos]
            if command == 99:
                break

            if command == 1:
                testProg[testProg[pos+3]] = testProg[testProg[pos+1]] + testProg[testProg[pos+2]]

            if command == 2:
                testProg[testProg[pos+3]] = testProg[testProg[pos+1]] * testProg[testProg[pos+2]]

            pos += 4

        if testProg[0] == target:
            print(testProg[0])
            print(noun*100+verb)