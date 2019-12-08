from collections import defaultdict

orbits = defaultdict(str)

with open("input") as infile:
    lines = infile.readlines()

for line in lines:
    orb, ing = line.split(")")


    orbits[ing[:-1]] = orb

def orb(obj):
    if orbits[obj] == "":
        return 0

    return 1 + orb(orbits[obj])

orbings = [x for x in orbits]

print(sum([orb(obj) for obj in orbings]))

"""
def num_orbs(thing):
    orbs = 0
    for other_thing in orbits[thing]:
        orbs += 1
        orbs += num_orbs(other_thing)

    return orbs

print(num_orbs("COM"))"""