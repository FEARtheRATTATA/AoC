def value(char):
        if char.isupper():
                return ord(char) - ord("A") + 27
        elif char.islower():
                return ord(char) - ord("a") + 1
        else:
                raise ValueError() 

def intersection(word1, word2):
        for char in set(word1).intersection(set(word2)):
                return char

def split_string(string):
        middle = len(string)//2
        return string[:middle], string[middle:]

def read(filename):
        with open(filename) as infile:
                return [word.strip() for word in infile.readlines()]


def part1():
        rucksacks = read("input")
        compartments = [split_string(sack) for sack in rucksacks]
        overlap = [intersection(*sack) for sack in compartments]
        values = [value(ov) for ov in overlap]
        print(sum(values))

def part2():
        rucksacks = read("input")
        badges = []
        for i in range(0, len(rucksacks), 3):
                for c in set(rucksacks[i]).intersection(set(rucksacks[i+1])).intersection(set(rucksacks[i+2])):
                        badges.append(value(c))
        print(sum(badges))

if __name__ == "__main__":
        part2()
