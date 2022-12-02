opp = {"A": 0, "B": 1, "C": 2}
self =  {"X": 0, "Y": 1, "Z": 2}



def score(their, mine):
        their = opp[their]
        mine = self[mine]
        score = mine+1
        outcome = 0
        if mine == (their+1)%3:
                outcome = 6
        if mine == their:
                outcome = 3

        score += outcome
        return score




def part2(their, mine):
        their = opp[their]
        mine = self[mine]
        

        if mine == 0:
                return (their+2)%3 + 1
        if mine == 1:
                return their + 4
        if mine == 2:
                return (their+1)%3 + 7
         


if __name__ == "__main__":
        points = 0
        with open("input.txt") as infile:
                for line in infile:
                        game = line.split()
                        points += part2(*game)
        print(points)
