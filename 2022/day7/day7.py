root = {
    "name": "/",
    "children": {
        "..": None
    },
    "files": []
}

root["children"]["/"] = root


working_dir = root

def add_dir(parent, name):
    """add a directory to the parent dir"""
    global root
    if name in parent["children"]:
        return parent["children"][name]

    new = {
        "name": name,
        "children": {
            "..": parent,
            "/": root
        },
        "files": []
    }

    parent["children"][name] = new
    return new

def cd(target):
    """Change working directory"""
    global working_dir, root
    if target not in working_dir["children"]:
        add_dir(working_dir, target)

    working_dir = working_dir["children"][target]

def add_file(size, filename):
    """Add a file to the current directory"""
    global working_dir
    if size == "dir":
        add_dir(working_dir, filename)

    else:
        size = int(size)
        working_dir["files"].append([filename, size])

def run_commands(commands):
    """Run the given commands"""
    for command in commands:
        command = command.split()
        if command[0] != "$":
            add_file(*command)

        elif command[1] == "ls":
            continue
        elif command[1] == "cd":
            cd(command[2])



low_total_size = []
def memcount(directory):
    """Count the total size of a given directory"""
    global low_total_size
    count = 0
    for file in directory["files"]:
        count += file[1]

    for subdir in directory["children"]:
        if subdir != ".." and subdir != "/":
            count += memcount(directory["children"][subdir])

    low_total_size.append([ directory["name"], count ])

    return count




def part1():
    """First part of the assignment"""
    global root, low_total_size
    with open("input") as infile:
        run_commands(infile.readlines())
    memcount(root)

    print(sum([directory[1] for directory in low_total_size if directory[1] < 100000]))




def part2():
    """Second part of the assignment"""
    global root, low_total_size
    with open("input") as infile:
        run_commands(infile.readlines())
    memcount(root)


    memvalues = [directory[1] for directory in low_total_size]
    total_space = 70000000
    free_space = total_space - max(memvalues)
    needed_space = 30000000 - free_space

    potential_files = [directory for directory in low_total_size if directory[1] >= needed_space]

    potential_files.sort(key = lambda x: x[1])
    
    print(potential_files)


def print_info(directory):
    print("Directory name: ", directory["name"])
    print("Subdirectories of ", directory["name"], ": ", directory["children"].keys())
    print("Files in ", directory["name"], ": ", directory["files"])
    print()

    for child in directory["children"]:
        if child != ".." and child != "/":
            print_info(directory["children"][child])


def main():
    #part1()
    part2()

if __name__ == '__main__':
    main()

