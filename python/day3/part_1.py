

# f = open("test_input.txt", "r")
f = open("input.txt", "r")

lines = f.readlines()

# print(lines)


# === Part 1 === #
# Finding the common items in each compartment #

def check_similar(first_part, second_part):
    res_char = None

    for char in first_part:
        if second_part.__contains__(char):
            res_char = char

    return res_char


def get_asci_value_char(char):
    if char.isupper():
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96


total_value = 0

for line in lines:
    first, second = line[:len(line) // 2], line[len(line) // 2:].strip("\n")

    similar_char = check_similar(first, second)
    value = get_asci_value_char(similar_char)

    total_value += value

print("Total Value part 1:", total_value)



