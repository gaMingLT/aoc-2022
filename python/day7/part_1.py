
# f = open("test_input.txt", "r")
f = open("input.txt", "r")

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
            if curr_directory != line[4:]:
                res["directories"].append(line[4:])
        else:
            size, file = line.split(' ')
            res["size"] += int(size)

    return res
    # return curr_directory, total_size, directories


def calculate_directory_size(directories):
    dir_values = []

    for xx in directories:
        value = compute_dirsize(xx)
        dir_values.append(value)

    return dir_values


# Adjusted from the youtube video here: https://www.youtube.com/watch?v=Io6AfTzadME
# It helped me see what whas wrong and I copied the code and adjusted to my values
def compute_dirsize(directory):
    dirsize = directory["size"]
    for ii in helper(directory["directories"], directories):
        if len(directory["directories"]) != 0:
            dirsize += compute_dirsize(ii)

    return dirsize


def helper(directory_names, directories):
    res = []
    for name in directory_names:
        for direc in directories:
            if name == direc["name"]:
                res.append(direc)
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

for item in directories: print(item)

dir_sizes = calculate_directory_size(directories)

sum_total = 0
for size in dir_sizes:
    if size <= 100000:
        sum_total += size

print("Part 1: ", sum_total)
