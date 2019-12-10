from part1 import *
import cmath as cm
from itertools import cycle
import pprint


pos = 0j
val = 0

for i in range(len(outp)):
    for j in range(len(outp[i])):
        if outp[i][j] > val:
            val = outp[i][j]
            pos = complex(i,j)
"""
print(val)
print(pos)
"""
test_pos = 9j
test_pos = 3

def angle(target):
    mod, vink = cm.polar(target - pos)
    return (-vink, -mod)

def ang(target):
    return cm.polar(target - pos)[1]


lst = [complex(x,y) for x in range(len(outp)) for y in range(len(outp[x])) if complex(x,y) != pos and map[x][y] == "#"]

lst.sort(key = angle)

curr_pos = 0
destr = 0


while True:
    curr_pos = curr_pos%len(lst)
    astr = lst[curr_pos]

    next_pos = (curr_pos+1)%len(lst)

    if abs(ang(lst[curr_pos]) - ang(lst[next_pos])) < 1e-6:
        curr_pos += 1

    else:
        destr += 1
        lst.pop(curr_pos)
        map[int(astr.real)][int(astr.imag)] = "."
        #print(astr)

        if destr == 200:
            print(astr)
            print(map)
            break

"""
    if lst[curr_pos][0] != lst[(curr_pos+1)%len(lst)][0]:
        destr += 1
        print(astr)
        if destr == 30:
            print(map)
            break

        lst.pop(curr_pos)
        map[int(astr.real)][int(astr.imag)] = "."


    else:
        curr_pos += 1
        curr_pos = curr_pos%len(lst)
"""