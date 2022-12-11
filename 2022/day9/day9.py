

def dist(num1, num2):
    diff = num1 - num2
    return max(abs(diff.real), abs(diff.imag))



def part1():
    with open("input") as infile:
        lines = infile.readlines()
    commands = [line.split() for line in lines]

    translation = {
        'R': 1j,
        'L': -1j,
        'U': 1,
        'D': -1
    }

    commands = [(translation[com[0]], int(com[1])) for com in commands]


    H = 0
    T = 0

    visited = {T}

    for direction, amount in commands:
        print(direction)
        print(amount)
        print(H)
        print(T)


        for i in range(amount):
            H += direction
            if dist(H, T) > 1:
                T = H - direction
                visited.add(T)

    print(len(visited))



    #print(commands)



def part2():
    with open("input") as infile:
        lines = infile.readlines()
    commands = [line.split() for line in lines]

    translation = {
        'R': 1j,
        'L': -1j,
        'U': 1,
        'D': -1
    }

    commands = [(translation[com[0]], int(com[1])) for com in commands]

    knots = [0 for _ in range(10)]
    
    visited = {knots[-1]}
    

    for direction, amount in commands:
        print(direction, amount)
        for _ in range(amount):
            knots[0] += direction

            for i in range(len(knots)-1):
                if dist(knots[i], knots[i+1]) > 1:
                    #knots[i+1] = knots[i] - direction
                    
                    diff = knots[i] - knots[i+1]

                    th_dir = 0

                    if diff.real != 0:
                        th_dir += diff.real/abs(diff.real)
    
                    if diff.imag != 0:
                        th_dir += diff.imag/abs(diff.imag) * 1j

                    

                    #print(knots[i], knots[i+1], th_dir)

                    knots[i+1] += th_dir



                else:
                    break

            visited.add(knots[-1])
    
        #print(knots)

    print(len(visited))



if __name__ == '__main__':
    #part1()
    part2()
