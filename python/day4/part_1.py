
# f = open("test_input.txt", "r")
f = open("input.txt", "r")

lines = f.readlines()

# print(lines)

# === Part 1 === #


def get_assigned_sections(start, end):
    res = []

    for i in range(start, end + 1):
        res.append(i)

    return res


def check_section_line(section_one_range, section_two_range):
    res = 0

    # Check if section two fits in section one
    if section_two_range[0] >= section_one_range[0] and section_two_range[-1] <= section_one_range[-1]:
        # print("Section two fits in section one", section_one_range, section_two_range)
        res = 1

    # Check if section one fits in section two
    elif section_one_range[0] >= section_two_range[0] and section_one_range[-1] <= section_two_range[-1]:
        #print("Section one fits in section two", section_one_range, section_two_range)
        res = 1

    else:
        # print("The sections don't overlap")
        res = 0

    return res


total_value = 0

for line in lines:
    section_one, section_two = line.split(',')
    # print(section_one, section_two)

    section_one_one, section_one_two = section_one.split('-')
    section_two_one, section_two_two = section_two.split('-')

    # print(section_one_one, section_one_two)
    # print(range(int(section_one_one), int(section_one_two)+1))

    one_assigned_sections = get_assigned_sections(int(section_one_one), int(section_one_two))
    # print("Part 1", one_assigned_sections)

    two_assigned_sections = get_assigned_sections(int(section_two_one), int(section_two_two))
    # print("Part 2", two_assigned_sections)

    value_to_add = check_section_line(one_assigned_sections, two_assigned_sections)
    total_value += value_to_add

print("Part 1: total value: ", total_value)
