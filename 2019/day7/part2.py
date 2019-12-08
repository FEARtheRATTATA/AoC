from part1 import compute

class Amplifier:
    def __init__(self, program, amp_val, give_inp, next_amp):
        self.program = program
        self.amp_val = amp_val
        self.give_inp = give_inp

        self.thing = True

        self.last_outp = ""
        self.pos = 0

    def __call__(self):


        if self.thing:
            self.thing = not self.thing
            return self.amp_val
        else:
            return self.give_inp

    def get_val(self):
        if self.thing:
            self.thing = not self.thing
            return self.amp_val
        else:
            return self.give_inp

    def run(self, inp):
        self.give_inp = inp

        while True:
            command = self.program[self.pos]
            parameter = command//100
            command = command%100

            if command == 99:
                return "A"
                self.pos += 1

            if command == 1:
                if parameter//100%10 == 0:
                    targPos = self.program[self.pos+3]
                else:
                    targPos = self.pos+3

                if parameter%10 == 0:
                    val1 = self.program[self.pos+1]
                else:
                    val1 = self.pos+1

                if parameter//10%10 == 0:
                    val2 = self.program[self.pos+2]
                else:
                    val2 = self.pos+2

                self.program[targPos] = self.program[val1] + self.program[val2]
                self.pos += 4

            if command == 2:
                if parameter//100%10 == 0:
                    targPos = self.program[self.pos+3]
                else:
                    targPos = self.pos+3

                if parameter%10 == 0:
                    val1 = self.program[self.pos+1]
                else:
                    val1 = self.pos+1

                if parameter//10%10 == 0:
                    val2 = self.program[self.pos+2]
                else:
                    val2 = self.pos+2

                self.program[targPos] = self.program[val1] * self.program[val2]
                self.pos += 4

            if command == 3:
                if parameter%10 == 0:
                    self.program[self.program[self.pos+1]] = int(self.get_val())
                else:
                    self.program[self.pos+1] = int(self.get_val())
                self.pos += 2

            if command == 4:
                if parameter%10 == 0:
                    v = self.program[self.program[self.pos+1]]
                else:
                    v = [self.program[self.pos+1]]
                self.pos += 2
                self.last_outp = v
                return v

            if command == 5:
                if parameter%10 == 0:
                    par1 = self.program[self.pos+1]
                else:
                    par1 = self.pos+1

                if parameter//10%10 == 0:
                    par2 = self.program[self.pos+2]
                else:
                    par2 = self.pos+2

                if self.program[par1] != 0:
                    self.pos = self.program[par2]
                else:
                    self.pos += 3

            if command == 6:
                if parameter%10 == 0:
                    par1 = self.program[self.pos+1]
                else:
                    par1 = self.pos+1

                if parameter//10%10 == 0:
                    par2 = self.program[self.pos+2]
                else:
                    par2 = self.pos+2

                if self.program[par1] == 0:
                    self.pos = self.program[par2]
                else:
                    self.pos += 3

            if command == 7:
                if parameter%10 == 0:
                    par1 = self.program[self.pos+1]
                else:
                    par1 = self.pos+1

                if parameter//10%10 == 0:
                    par2 = self.program[self.pos+2]
                else:
                    par2 = self.pos+2

                if parameter//100%10 == 0:
                    par3 = self.program[self.pos+3]
                else:
                    par2 = self.pos+3

                if self.program[par1] < self.program[par2]:
                    self.program[par3] = 1
                else:
                    self.program[par3] = 0

                self.pos += 4

            if command == 8:
                if parameter%10 == 0:
                    par1 = self.program[self.pos+1]
                else:
                    par1 = self.pos+1

                if parameter//10%10 == 0:
                    par2 = self.program[self.pos+2]
                else:
                    par2 = self.pos+2

                if parameter//100%10 == 0:
                    par3 = self.program[self.pos+3]
                else:
                    par2 = self.pos+3

                if self.program[par1] == self.program[par2]:
                    self.program[par3] = 1
                else:
                    self.program[par3] = 0

                self.pos += 4


if __name__ == "__main__":

    from itertools import permutations, cycle

    target = 19690720

    with open("input") as infile:
        program = [int(x) for x in infile.readline().split(',')]

        """
    program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
"""

    sols = {}


    for perm in permutations([5,6,7,8,9]):

        amps = [Amplifier(program.copy(), x, 0, 0) for x in perm]

        for i in range(len(amps)-1):
            amps[i].next_amp = amps[i+1]

        amps[-1].next_amp = amps[0]


        a = 0

        for amp in cycle(amps):
            if a == "A":
                break

            #print(a)
            a = amp.run(a)

        sols[amps[-1].last_outp] = perm


    max_outp = max(sols.keys())
    print(max_outp)
    print(sols[max_outp])