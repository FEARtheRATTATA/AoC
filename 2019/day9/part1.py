class Computer:
    def __init__(self, program):
        self.program = program

        self.last_outp = ""
        self.pos = 0
        self.rel_base = 0

    def get_val(self):
        """
        if self.thing:
            self.thing = not self.thing
            return self.amp_val
        else:
            return self.give_inp
        """

        return input()


    def mode_pos(self, i, shift):
        if i == 0:
            return self.program[self.pos+shift]

        if i == 1:
            return self.pos+shift

        if i == 2:
            return self.program[self.pos+shift] + self.rel_base


    def run(self):

        while True:
            command = self.program[self.pos]
            parameter = command//100
            command = command%100



            if command == 1:
                targPos = self.mode_pos(parameter//100%10, 3)
                val1 = self.mode_pos(parameter%10, 1)
                val2 = self.mode_pos(parameter//10%10, 2)

                self.program[targPos] = self.program[val1] + self.program[val2]
                self.pos += 4

            elif command == 2:
                targPos = self.mode_pos(parameter//100%10, 3)
                val1 = self.mode_pos(parameter%10, 1)
                val2 = self.mode_pos(parameter//10%10, 2)

                self.program[targPos] = self.program[val1] * self.program[val2]
                self.pos += 4

            elif command == 3:
                a = self.mode_pos(parameter%10, 1)
                self.program[a] = int(self.get_val())
                self.pos += 2

            elif command == 4:
                v = self.mode_pos(parameter%10, 1)
                v = self.program[v]
                self.pos += 2
                self.last_outp = v
                print(v)

            elif command == 5:
                par1 = self.mode_pos(parameter%10, 1)
                par2 = self.mode_pos(parameter//10%10, 2)

                if self.program[par1] != 0:
                    self.pos = self.program[par2]
                else:
                    self.pos += 3

            elif command == 6:
                par1 = self.mode_pos(parameter%10, 1)
                par2 = self.mode_pos(parameter//10%10, 2)

                if self.program[par1] == 0:
                    self.pos = self.program[par2]
                else:
                    self.pos += 3

            elif command == 7:
                par1 = self.mode_pos(parameter%10, 1)
                par2 = self.mode_pos(parameter//10%10, 2)
                par3 = self.mode_pos(parameter//100%10, 3)

                if self.program[par1] < self.program[par2]:
                    self.program[par3] = 1
                else:
                    self.program[par3] = 0

                self.pos += 4

            elif command == 8:
                par1 = self.mode_pos(parameter%10, 1)
                par2 = self.mode_pos(parameter//10%10, 2)
                par3 = self.mode_pos(parameter//100%10, 3)

                if self.program[par1] == self.program[par2]:
                    self.program[par3] = 1
                else:
                    self.program[par3] = 0

                self.pos += 4

            elif command == 9:
                par = self.mode_pos(parameter%10, 1)

                self.rel_base += self.program[par]
                self.pos += 2

            else:
                assert command == 99
                return "A"
                self.pos += 1





with open("input") as infile:
    program = [int(x) for x in infile.readline().split(',')]

for i in range(1000):
    program.append(0)

a = Computer(program.copy())
a.run()