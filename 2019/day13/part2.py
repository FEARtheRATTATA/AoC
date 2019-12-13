import numpy as np
import matplotlib.pyplot as plt

class Computer:
    def __init__(self, program, inp_fun):
        self.program = program
        self.inp_fun = inp_fun

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
                self.program[a] = int(self.inp_fun())
                self.pos += 2

            elif command == 4:
                v = self.mode_pos(parameter%10, 1)
                v = self.program[v]
                self.pos += 2
                self.last_outp = v
                return v

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

program[0] = 2



outp = ""

disp = np.zeros((50, 30))
ball_pos = (0,0)
paddle_pos = (0,0)
def inp():
    global disp, ball_pos, paddle_pos
    if ball_pos[0] > paddle_pos[0]:
        return 1
    elif ball_pos[0] < paddle_pos[0]:
        return -1
    else:
        return 0

CPU = Computer(program, inp)



while outp != "A":
    x = CPU.run()
    if x == "A":
        break

    y = CPU.run()
    t_id = CPU.run()

    if x == -1 and y == 0:
        print(t_id)
    else:
        disp[x][y] = t_id
        if t_id == 4:
            ball_pos = (x, y)

        if t_id == 3:
            paddle_pos = (x, y)


plt.imshow(disp)
plt.show()