from part_1 import get_asci_value_char

# f = open("test_input.txt", "r")
f = open("input.txt", "r")

lines = f.readlines()


# === Part 2 === #

def check_similar(first, second, third):
    res_char = None

    for char in first:
        if second.__contains__(char) and third.__contains__(char):
            res_char = char

    return res_char


total_value = 0
counter = 0
buffer_lines = []

for line in lines:
    buffer_lines.append(line.strip('\n'))

    if len(buffer_lines) == 3:
        similar_char = check_similar(buffer_lines[0], buffer_lines[1], buffer_lines[2])

        value = get_asci_value_char(similar_char)
        total_value += value

        buffer_lines = []

print("Total Value part 2: ", total_value)
