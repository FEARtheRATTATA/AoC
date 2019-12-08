import numpy as np
from collections import defaultdict

with open("input") as infile:
    vals = infile.readlines()
test = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"

pos = 0
a = set()
crossings = set()

positions = defaultdict(complex)

def move(inp, plll):
    global pos, a
    dir = {
        'U': 1j,
        'D': -1j,
        'L': -1,
        'R': 1
    }

    mov = dir[inp[0]]
    for i in range(int(inp[1:])):
        pos += mov
        positions[pos] += plll

lines = []
plll = 1
for line in vals:
    for mov in line.split(","):
        move(mov, plll)

    lines.append(a)
    a = set()
    pos = 0
    plll = 1j

crossings = [k for k,v in positions.items() if v.real >= 1 and v.imag >= 1]
print(min([abs(x.real)+abs(x.imag) for x in crossings]))