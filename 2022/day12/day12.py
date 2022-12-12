from collections import deque


def adjacent(char1, char2):
    if char1 == 'S':
        return char2 == 'a'
    
    if char2 == 'E':
        return char1 == 'z'

    if ord(char2) - ord(char1) <= 1:
        return True

    return False





def part1(grid, start):
    visited = {start}
    path = deque()
    path.append((start, 0, [start]))

    while path:
        pos, length, partial_path = path.pop()
        #print(pos, length)

        pos_char = grid[int(pos.real)][int(pos.imag)]


        if pos_char == 'E':
            return pos, length, partial_path

        for direction in (1, -1, 1j, -1j):
            new_pos = pos + direction

            if new_pos.real < 0 or new_pos.imag < 0:
                continue

            try:
                new_pos_char = grid[int(new_pos.real)][int(new_pos.imag)]
            except:
                continue
            #print(pos, new_pos, pos_char, new_pos_char)
            if new_pos in visited:
                continue

            #print(new_pos, pos_char, new_pos_char)

            if adjacent(pos_char, new_pos_char):
                #print(pos, new_pos, pos_char, new_pos_char)
                visited.add(new_pos)

                path.appendleft((new_pos, length+1, partial_path + [new_pos]))






def print_grid(grid):
    for line in grid:
        print(''.join(line))
    

if __name__ == '__main__':
    with open("input") as infile:
        lines = infile.readlines()


    grid = [list(s.strip()) for s in lines]

    print_grid(grid)
    start = -1 - 1j

    starts = []

    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y in {'S', 'a'}:
                start = i + j*1j

                starts.append((start, part1(grid, start)))


    starts = [c[:2] for c in starts if c[1] is not None]

    print(starts)

    print(min(starts, key=lambda x: x[1][1]))

    print([grid[int(c[0].real)][int(c[0].imag)] for c in starts])


    #start = 3+0j

    #print(part1(grid, start))
