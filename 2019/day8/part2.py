import numpy as np

with open("input") as infile:

    program = infile.readline()
    wide = 25
    tall = 6
    """
    program = "0222112222120000"
    wide = 2
    tall = 2
    """

ptr = 0
layers = []
while ptr < len(program):
    column = []
    for _ in range(tall):
        row = []
        for __ in range(wide):
            row.append(program[ptr])
            ptr += 1

        column.append(row)

    layers.append(column)


color = np.full((tall,wide), 2)

for layer in layers:
    for i in range(tall):
        for j in range(wide):
            if color[i][j] == 2:
                color[i][j] = layer[i][j]

print(color)