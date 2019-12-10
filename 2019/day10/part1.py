from fractions import gcd
import numpy as np

with open("input") as infile:
    map = [[x for x in line[:-1]] for line in infile.readlines()]

def ast_bet(map, pos1, pos2):
    dist = pos2-pos1
    move = dist/gcd(abs(dist.real), abs(dist.imag))

    cur_pos = pos1+move
    while cur_pos != pos2:
        if map[int(cur_pos.imag)][int(cur_pos.real)] == '#':
            return True

        cur_pos += move

    return False

#print(ast_bet(map, 0j, 4))

outp = np.zeros_like(map, dtype = int)

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '#':
            for k in range(len(map)):
                for l in range(len(map[k])):
                    if k == i and j == l:
                        continue

                    if map[k][l] == '#':

                        if ast_bet(map, complex(j, i), complex(l, k)):
                            continue

                        outp[i][j] += 1


if __name__ == "__main__":
    print(max([max(i) for i in outp]))