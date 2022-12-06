
# f = open("test_input.txt", "r")
f = open("input.txt", "r")

lines = f.readlines()

# print(lines)


# === Part 1 ===

def buffer_of_four_characters(line) -> int:
    buffer = []

    counter = 0

    for char in line:
        buffer.append(char)

        # part 1 set buffer to 4 & part 2 set buffer to 14
        if len(buffer) == 14:

            # check buffer if not, remove one and next one
            buffer_check = check_buffer(buffer)

            # remove one character and add new one in next pass and check
            if buffer_check:
                buffer.pop(0)
            else:
                return counter+1

        counter += 1

    return 0


def check_buffer(buffer):
    duplicate = False

    seen = set()
    for n in buffer:
        if n in seen:
            duplicate = True
            # print("duplicate:", n)
        else:
            seen.add(n)

    return duplicate


# If you want to check each test input, change the index
line_to_check = lines[0].strip('\n')
# print(line_to_check)

index = buffer_of_four_characters(line_to_check)
print("Index: ", index)
