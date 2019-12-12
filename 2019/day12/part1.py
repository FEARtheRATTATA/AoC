import numpy as np

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

with open("input") as infile:
    moons = []
    for line in infile.readlines():
        moons.append(Moon(line[1:-2]))


for i in range(1000):
    for moon in moons:
        for other_moon in moons:
            moon.interact(other_moon)

    for moon in moons:
        moon.update_pos()


print(sum([moon.total_energy() for moon in moons]))