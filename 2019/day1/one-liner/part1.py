print(sum([(lambda num: num//3-2)(int(line)) for line in open("input").readlines()]))