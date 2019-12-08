with open("input") as infile:
    """
    program = infile.readline()
    wide = 25
    tall = 6
    """
    program = "123456789012"
    wide = 3
    tall = 2


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

#print(layers)

zeros = {}
for n, lay in enumerate(layers):
    zeros[sum([x.count('0') for x in lay])] = n

min_zers = min(zeros.keys())
min_layer = zeros[min_zers]
print(sum([x.count('1') for x in layers[min_layer]]) *
      sum([x.count('2') for x in layers[min_layer]]))