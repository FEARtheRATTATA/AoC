





if __name__ == "__main__":
        with open("input") as infile:
                lines = infile.readlines()

        lines = [line.strip().split(",") for line in lines]
        lines = [[sec.split("-") for sec in line] for line in lines]
        lines = [[[int(sec) for sec in pair] for pair in line] for line in lines]
        lines = [sorted(line, key = lambda x: x[0]) for line in lines]
        
        #print(lines)
       

        n = 0

        for line in lines:
                if line[0][0] == line[1][0]:
                        n += 1
                elif line[0][1] >= line[1][1]:
                        n += 1
        print("part 1:", n)




        n = 0
        
        for line in lines:
                if line[0][1] >= line[1][0]:
                        n += 1
        
        print("part 2:", n)
