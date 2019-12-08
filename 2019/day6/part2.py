from collections import defaultdict

orbits = defaultdict(str)

with open("input") as infile:
    lines = infile.readlines()

for line in lines:
    orb, ing = line.split(")")


    orbits[ing[:-1]] = orb

def num(objA, objB):
    if objA == "":
        return -1

    if objA == objB:
        return 0

    val = num(orbits[objA], objB)
    if val == -1:
        return -1
    return 1 + val



def to_santa(obj):
    target = "SAN"

    santa_orbit = []

    while target != "":
        santa_orbit.append(target)
        target = orbits[target]

    for val,let in enumerate(santa_orbit):
        ans = num(obj,let)
        if ans != -1:
            print(ans+val)


to_santa("YOU")