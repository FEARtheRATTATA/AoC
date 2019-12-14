
for i in range(4906796, 50000000):
    have = {'FUEL': 0}
    reactions = {}

    exec(f"""from math import ceil

with open("input") as infile:
    reactions = {reactions}
    for line in infile.readlines():
        line = line.split("=>")
        res = line[1].split()
        product = res[1]
        amount = res[0]
        reqs = line[0].split(",")
        reactions[product] = (amount, reqs)

reqs = []
reqs.append(({i}, "FUEL"))
ore = 0

have = {have}
ore = 0

while len(reqs) > 0:
    num, item = reqs.pop()
    num = int(num)
    if item == "ORE":
        ore += num
        continue

    rec = reactions[item]

    needed = num - have[item]
    created = int(rec[0])
    reacts_needed = ceil(needed/created)


    have[item] += created * reacts_needed

    for need in rec[1]:
        num_s, item_s = need.split()
        num_s = int(num_s) * reacts_needed

        if item_s not in have:
            have[item_s] = 0

        reqs.append((num_s, item_s))

    have[item] -= num



print(ore)""")