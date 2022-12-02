
f = open("input.txt", "r")
# f = open("test_input.txt", "r")

lines = f.readlines()

elves = []
number_highest = None
current_elf = None

for line in lines:
    split_line = line.split('\n')
    calories = split_line[0]

    if calories.isdigit():
        calories = int(calories)
        print("Number", calories)

        if current_elf is None:
            current_elf = (len(elves) + 1, calories, 1)
        else:
            current_elf = (current_elf[0], current_elf[1] + calories, current_elf[2] + 1)

    else:
        print("Spacing", current_elf)

        elves.append(current_elf)

        current_elf = None

if current_elf is not None:
    print("Last elf", current_elf)
    elves.append(current_elf)

print("Elves", elves)

sorted_elves = sorted(elves, key=lambda a: a[1], reverse=True)
print("Sorted", sorted_elves)

print("Result", sorted_elves[0])

# --- Part 2 --- #

print("# --- Part 2 --- #")

top3_elves = sorted_elves[0:3]
print("Top 3:", top3_elves)

total = 0

for elf in top3_elves:
    total += elf[1]

print("Total", total)
