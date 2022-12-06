def part1(tokenstream):
        for i in range(len(tokenstream) - 4):   
                print(tokenstream[i:i+4])
                token = tokenstream[i:i+4]

                if len(set(token)) == 4:
                        return i


#def part2(tokenstream):
        
def part1(tokenstream):
        for i in range(len(tokenstream) - 14):   
                print(tokenstream[i:i+14])
                token = tokenstream[i:i+14]

                if len(set(token)) == 14:
                        return i

if __name__ == "__main__":
        with open("input") as infile:
                tokens = infile.readline().strip()

        print(part1(tokens)+4)
        print(part1(tokens)+14)
