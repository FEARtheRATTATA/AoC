from collections import deque
import re

class Monkey:
    def __init__(self, index, starting_items, operation, test, target):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.target = target
        self.monkeys = []
        self.index = index


        self.inspected = 0



    def set_monkeys(self, monkeys):
        self.monkeys = monkeys

    def receive(self, item):
        self.items.append(item)


    def operate(self, item):
        #print(self.operation)

        if self.operation[0] == "old":
            first = lambda x: x
        else: 
            first = lambda x: int(self.operation[0])

        if self.operation[2] == "old":
            second = lambda x: x
        else:
            second = lambda x: int(self.operation[2])


        if self.operation[1] == '+':
            op = lambda x: first(x) + second(x)

        else:
            op = lambda x: first(x) * second(x)

        opp = lambda x: op(x) // 3


        return opp(item)



    def throw(self):
        #print(f"Monkey number {self.index} currently has items: {self.items}")
        while len(self.items) > 0:


            item = self.items.pop(0)
            #print(f"Inspecting item {item}")
            item = self.operate(item)
            result = item % self.test == 0
            #print(f"Worry level is now {item}. Whether it divides {self.test}: {result}")
            target = self.monkeys[self.target[0]] if result else self.monkeys[self.target[1]]
            
            #print(f"Throwing item to monkey #{target.index}")

            self.inspected += 1


            target.receive(item)

class Monkey2(Monkey):

    def set_monkeys(self, monkeys):
        self.monkeys = monkeys
        p = 1
        for monkey in monkeys:
            p *= monkey.test

        self.p = p


    def operate(self, item):
        if self.operation[0] == "old":
            first = lambda x: x
        else: 
            first = lambda x: int(self.operation[0])

        if self.operation[2] == "old":
            second = lambda x: x
        else:
            second = lambda x: int(self.operation[2])


        if self.operation[1] == '+':
            op = lambda x: first(x) + second(x)

        else:
            op = lambda x: first(x) * second(x)

        opp = lambda x: op(x) % self.p


        return opp(item)



def part1(monkey_list):
    for i in range(20):
        print(i)
        for monkey in monkey_list:
            monkey.throw()

        for monkey in monkey_list:
            print(monkey.index, monkey.items)



    

    monkey_list.sort(key = lambda m: m.inspected)
    for monkey in monkey_list:
        print(monkey.inspected)


    print(monkey_list[-1].inspected * monkey_list[-2].inspected)


def part2(monkey_list):
    for i in range(10000):
        print(i)
        for monkey in monkey_list:
            monkey.throw()

        #for monkey in monkey_list:
        #    print(monkey.index, monkey.items)



    

    monkey_list.sort(key = lambda m: m.inspected)
    for monkey in monkey_list:
        print(monkey.inspected)


    print(monkey_list[-1].inspected * monkey_list[-2].inspected)



def main():
    with open("input") as infile:
        lines = infile.read().strip()

    monkeys = lines.split("\n\n")


    monkey_list = []
    
    for monkey in monkeys:
        lines = [line.strip() for line in monkey.split('\n')]

        print(lines)

        number = re.findall(r'Monkey (\d):', lines[0])
        number = int(number[0])
        print(number)
        
        
        starting_items = re.findall(r'Starting items: (.*)', lines[1])
        print(starting_items)
        starting_items = [int(item) for item in starting_items[0].split(', ')]
        print(starting_items)

        
        operation = re.findall(r'Operation: new = (old|\d+) (\+|\*) (old|\d+)', lines[2])[0]
        print(operation)
        
        if operation[0] == "old":
            first = lambda x: x
        else: 
            first = lambda x: int(operation[0])

        if operation[2] == "old":
            second = lambda x: x
        else:
            second = lambda x: int(operation[2])


        if operation[1] == '+':
            op = lambda x: first(x) + second(x)

        else:
            assert operation[1] == '*'
            op = lambda x: first(x) * second(x)

        opp = lambda x: op(x) // 3

        
        test = re.findall(r'Test: divisible by (\d+)', lines[3])
        d_by = int(test[0])
        print("d_by: ", d_by)



        
        target1 = re.findall(r'If true: throw to monkey (\d+)', lines[4])
        target2 = re.findall(r'If false: throw to monkey (\d+)', lines[5])
        
        target = (int(target1[0]), int(target2[0]))
        print(target)


        monkey = Monkey2(number, starting_items, operation, d_by, target)
        
        
        print(monkey)
        assert len(monkey_list) == number
        monkey_list.append(monkey)
        


    for monkey in monkey_list:
        monkey.set_monkeys(monkey_list)
    
    part2(monkey_list)


if __name__ == '__main__':
    main()

