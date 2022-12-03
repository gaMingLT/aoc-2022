

# f = open("test_input.txt", "r")
f = open("input.txt", "r")

lines = f.readlines()

print(lines)


# === Part 1 === #
# Finding the common items in each compartment #

def check_similar(firstpart, secondpart):

    similar_char = None

    for char in firstpart:
        if secondpart.__contains__(char):
            similar_char = char

    return similar_char


def get_asci_value_char(char):
    if char.isupper():
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96

total_value = 0

for line in lines:
    firstpart, secondpart = line[:len(line) // 2], line[len(line) // 2:].strip("\n")

    #print(firstpart, secondpart)

    similar_char = check_similar(firstpart, secondpart)
    #print(similar_char)

    value = get_asci_value_char(similar_char)
    # print(value)

    total_value += value

print("Total Value:", total_value)



