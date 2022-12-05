def read_input(filename):
        with open(filename) as infile:
                lines = list(infile.readlines())
        n = -1
        a = -1
        for k, line in enumerate(lines):
                l = line.split()
                try:
                        if line[1] != '1':
                                pass
                        l = [int(i) for i in l]
                        if len(l) > 0:
                                n = len(l)
                                a = k
                except:
                        pass
        #print(n)
        stacks = [[] for _ in range(n)]
        for line in lines:
                if line[1] == '1':
                        break
                #print(line)
                for i in range(n):
                        #print(line[4*i+1])
                        if line[4*i+1] != ' ':
                                stacks[i].append(line[4*i+1])

        #print(stacks)
        commands = []
        for line in lines[a+2:]:
                #print(line.strip())
                words = line.split()
                command = [int(words[1]), int(words[3]), int(words[5])]
                commands.append(command)
        return stacks, commands


def part1(stacks, commands):
        for command in commands:
                for i in range(command[0]):
                        print(stacks, command)
                        stacks[command[2]-1].insert(0, stacks[command[1]-1].pop(0))
        
        return stacks




def part2(stacks, commands):    
        for command in commands:
                n = command[0]
                fr = command[1]-1
                to = command[2]-1
                print(stacks, command)           
                moved = stacks[fr][:n]
                stacks[fr] = stacks[fr][n:]
                stacks[to] = moved + stacks[to]
                print(stacks)
        print("".join([stack[0] for stack in stacks]))

if __name__ == "__main__":
        stacks, commands = read_input("input")
        print(stacks)
        print(commands)
        print(part2(stacks, commands))
