import numpy as np
from math import gcd
import sys

class Moon:
    def __init__(self, data):
        self.pos = np.array([int(dat[2:]) for dat in data.split(', ')])
        self.vel = np.array([0,0,0])

    def interact(self, other):
        for i in range(3):
            if self.pos[i] > other.pos[i]:
                self.vel[i] -= 1
            elif self.pos[i] < other.pos[i]:
                self.vel[i] += 1
            else:
                assert self.pos[i] == other.pos[i]

    def update_pos(self):
        self.pos += self.vel

    def pot_energy(self):
        return sum(abs(self.pos))

    def kin_energy(self):
        return sum(abs(self.vel))

    def total_energy(self):
        return self.pot_energy()*self.kin_energy()



dims = [set(), set(), set()]

with open("input") as infile:
    moons = []
    for line in infile.readlines():
        moons.append(Moon(line[1:-2]))

x_x_x = y_y_y = z_z_z = True
reps = []
for i in range(1000000):
    for moon in moons:
        for other_moon in moons:
            moon.interact(other_moon)

    for moon in moons:
        moon.update_pos()

    if x_x_x:
        xs = tuple((moon.pos[0], moon.vel[0]) for moon in moons)
        if xs in dims[0]:
            reps.append(i)
            x_x_x = False
        else:
            dims[0].add(xs)

    if y_y_y:
        ys = tuple((moon.pos[1], moon.vel[1]) for moon in moons)
        if ys in dims[1]:
            reps.append(i)
            y_y_y = False
        else:
            dims[1].add(ys)

    if z_z_z:
        zs = tuple((moon.pos[2], moon.vel[2]) for moon in moons)
        if zs in dims[2]:
            reps.append(i)
            z_z_z = False
        else:
            dims[2].add(zs)

    if not (x_x_x or y_y_y or z_z_z):
        break

print(reps)
i = reps[0]
while(True):
    if i%reps[1] == 0:
        print(i)
        break

    i += reps[0]

val = i
while(True):
    if i%reps[2] == 0:
        print(i)
        break

    i += val