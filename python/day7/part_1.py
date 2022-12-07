
f = open("test_input.txt", "r")
# f = open("input.txt", "r")

lines = f.readlines()

# print(lines)


# === Part 1 ===

def parse_command(command, curr_directory):
    command_type = command[0:2]
    directory = curr_directory
    list_contents = False

    if command_type == "cd":
        # print("Change directory", command[2:])
        directory = command[3:]
    elif command_type == "ls":
        # print("Listing directory contents")
        list_contents = True

    return directory, list_contents


def parse_directory_listing(curr_directory, line_buffer):
    res = {"name": curr_directory, "size": 0, "directories": []}

    for line in line_buffer:
        if line[0] == "d":
            res["directories"].append(line[4:])
        else:
            size, file = line.split(' ')
            res["size"] += int(size)

    return res
    # return curr_directory, total_size, directories


def calculate_directory_size(directories):

    size, sizes = new_dir_size(directories[0]["name"], {}, directories)
    print(sizes)

    return directories


def new_dir_size(name, finals, directories):
    size = 0
    for directory in directories:
        if len(directory["directories"]) != 0:
            dir_size, finals = new_dir_size(directory["name"], finals, helper(directory["name"], directory["directories"], directories))
            size += dir_size
        else:
            size += int(directory["size"])

    finals[name] = size
    return size, finals


def helper(name, directory_names, directories):
    res = []
    for name in directory_names:
        for direc in directories:
            if name == direc["name"]:
                res.append(direc)
    #print("Helper", name, res)
    return res


# (directory-name, size, [other-directories-array])
previous_directory = ""
current_directory = ""
directories = []
list_directory_contents = False
directory_listening_buffer = []

for line in lines:
    line = line.strip('\n')

    if not list_directory_contents and len(directory_listening_buffer) > 0:
        directories.append(parse_directory_listing(previous_directory, directory_listening_buffer))
        directory_listening_buffer = []

    if line[0] == '$':
        previous_directory = current_directory
        current_directory, list_directory_contents = parse_command(command=line[2:], curr_directory=current_directory)
    elif list_directory_contents:
        directory_listening_buffer.append(line)


# Capture last buffer
if len(directory_listening_buffer) >= 0:
    directories.append(parse_directory_listing(current_directory, directory_listening_buffer))
    directory_listening_buffer = []

print(directories)
directories2 = calculate_directory_size(directories)
# print(directories2)

# total_size = 0
#
# for direc2 in directories2:
#     if direc2[1] <= 100000:
#         total_size += direc2[1]
#
# print("Part 1: ", total_size)
