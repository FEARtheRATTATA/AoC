from math import prod


visible = set()




def check(grid, direction, pos):
    global visible
    largest = -1
    #print(direction)
    while True:
        #print(pos)
        try:
            if grid[int(pos.real)][int(pos.imag)] > largest:
                visible = visible.union({pos})
                largest = grid[int(pos.real)][int(pos.imag)]
        except:
            return

        pos += direction


def check_mod(grid, direction, pos, top):
    global visible
    while True:
        if pos.real < 0 or pos.imag < 0:
            return


        try:
            if grid[int(pos.real)][int(pos.imag)] >= top:
                visible = visible.union({pos})

                return

            visible = visible.union({pos})
        except:
            return

        pos += direction
        

def scenic_score(grid, tree):
    global visible
    scores = []
    #visible = set()
    for direction in (1, -1j, -1, 1j):
        #print(direction, tree)
        visible = set()
        check_mod(grid, direction, tree + direction, grid[int( tree.real )][int( tree.imag )])
        print(tree, visible)
        #if len(visible) != 0:
        scores.append(len(visible))



    print(tree, scores, prod(scores))

    return prod(scores)

if __name__ == '__main__':
    grid = []
    with open("input") as infile:
        for line in infile.readlines():
            ints = [int(c) for c in line.strip()]
            grid.append(ints)


    print(grid)
    pos = 0 + 0j
    print(grid[int(pos.real)][int(pos.imag)])

    direction = 1 + 0j
    
    for i in range(len(grid[0])):
        check(grid, direction, i*1j)


    direction = -1 + 0j

    for i in range(len(grid[0])):
        check(grid, direction, len(grid)-1 + i*1j)


    direction = 0 + 1j

    for i in range(len(grid)):
        check(grid, direction, i)

    direction = 0 - 1j

    for i in range(len(grid)):
        check(grid, direction, i + (len(grid[i]) - 1)*1j)



    print(visible)
    print(len(visible))


    scores = []
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            print(i + k*1j)
            scores.append(scenic_score(grid, i + k*1j))

    print(max(scores))
