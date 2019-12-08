with open("input.txt") as infile:
    inp = infile.readline().split("-")
total = 0

for i in range(int(inp[0]), int(inp[1])):
    num = list(map(int, str(i)))
    if not all(num[i] <= num[i+1] for i in range(len(num)-1)):
        continue

    j = 0
    while j < len(num) - 1:
        if num[j] == num[j+1]:
            if j < len(num) - 2:
                if num[j] != num[j+2]:
                    total += 1
                    break
                else:
                    i = j
                    try:
                        while num[i] == num[j]:
                            j += 1
                    except:
                        continue
                    continue
            else:
                total += 1
                break
        j += 1


print(total)