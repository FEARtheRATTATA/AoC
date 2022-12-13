def compare(lst1, lst2):
    if len(lst1) == 0:
        if len(lst2) == 0:
            return 0
        return 1
    
    if len(lst2) == 0:
        return -1


    #print(f"Comparing {lst1} with {lst2}")

    if isinstance(lst1[0], int) and isinstance(lst2[0], int):
        #print(f"Both are integers! Comparing {lst1[0]} with {lst2[0]}")
        if lst1[0] < lst2[0]:
            #print("Correct order!")
            return 1
        if lst1[0] > lst2[0]:
            #print("Wrong order!")
            return -1

        #print("Equal - requires further investifation!")
        return compare(lst1[1:], lst2[1:])

    if isinstance(lst1[0], int):
        first = [lst1[0]]

    else:
        first = lst1[0]

    if isinstance(lst2[0], int):
        second = [lst2[0]]

    else:
        second = lst2[0]

    
    partial = compare(first, second)

    if partial == 0:
        return compare(lst1[1:], lst2[1:])
    else:
        return partial






def part1(pairs):
    correct = []

    for i, pair in enumerate(pairs):
        if compare(*pair) == 1:
            correct.append(i + 1)

    print(sum(correct))


from itertools import chain
from functools import cmp_to_key
import math

def part2(pairs):
    pairs = pairs + [[[[2]], [[6]]]]
    lsts = list(chain(*pairs))
    lsts = sorted(lsts, key = cmp_to_key(compare), reverse = True)

    print(lsts)

    dividers = []

    for i, lst in enumerate(lsts):
        if compare(lst, [[6]]) == 0 or compare(lst, [[2]]) == 0:
            dividers.append(i+1)

    print(dividers)

    print(math.prod(dividers))



if __name__ == '__main__':
    with open("input") as infile:
        pairs = infile.read().split('\n\n')

    pairs = [pair.split('\n') for pair in pairs]

    pairs = [[eval(lst[0]), eval(lst[1])] for lst in pairs]


    #print(pairs)

    #part1(pairs)
    part2(pairs)
