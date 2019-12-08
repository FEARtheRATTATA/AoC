with open("input.txt") as infile:
    inp = infile.readline().split("-")
total = 0

for i in range(int(inp[0]), int(inp[1])):
    num = list(map(int, str(i)))
    if not all(num[i] <= num[i+1] for i in range(len(num)-1)):
        continue

    for j in range(len(num)-1):
        if num[j] == num[j+1]:
            total += 1
            break

print(total)