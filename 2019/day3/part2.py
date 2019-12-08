import numpy as np
from collections import defaultdict

with open("input") as infile:
    vals = infile.readlines()
test = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"

pos = 0
a = set()
crossings = set()

positions = defaultdict(complex)


plllDir = 1
plll = 0

def move(inp):
    global pos, a, plll, plllDir
    dir = {
        'U': 1j,
        'D': -1j,
        'L': -1,
        'R': 1
    }

    mov = dir[inp[0]]
    for i in range(int(inp[1:])):
        pos += mov
        plll += plllDir
        positions[pos] += plll

lines = []
for line in vals:
    for mov in line.split(","):
        move(mov)

    lines.append(a)
    a = set()
    pos = 0
    plll = 0j
    plllDir = 1j

crossings = [(k,v) for k,v in positions.items() if v.real >= 1 and v.imag >= 1]
print(min([abs(x[1].real)+abs(x[1].imag) for x in crossings]))