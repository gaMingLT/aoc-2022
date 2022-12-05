
# f = open("test_input.txt", "r")
f = open("input.txt", "r")

lines = f.readlines()

# print(lines)

# === Part 2 === #


def get_amount_of_stacks_and_index(stack_lines):
    to_array = [char for char in stack_lines[-1]]

    res = []

    for index, test in enumerate(to_array):
        if test != ' ':
            res.append((int(test),index))

    return res


def tranform_stack_lines(stack_lines):
    stack_lines.remove('')
    stack_numbers_and_index = get_amount_of_stacks_and_index(stack_lines)

    stack_array = []

    for numbers_and_index in stack_numbers_and_index:
        for stack_line in stack_lines[:-1]:
            if len(stack_line) >= numbers_and_index[1] and stack_line[numbers_and_index[1]] != ' ':

                if len(stack_array) < numbers_and_index[0]:
                    stack_array.append([stack_line[numbers_and_index[1]]])
                else:
                    stack_array[numbers_and_index[0]-1].append(stack_line[numbers_and_index[1]])


    for index, stack_line in enumerate(stack_array):
        stack_array[index] = stack_array[index][::-1]

    return stack_array



def transform_move_lines(move_lines):
    res = []

    for move_line in move_lines:
        splitted = move_line.split(' ')
        amount_to_move = splitted[1]
        src_loc = splitted[3]
        dst_loc = splitted[-1]

        res.append((amount_to_move, src_loc, dst_loc))

    return res



def execute_moves(stacks, moves):

    for move in moves:
        amount_to_move, src_loc, dst_loc = int(move[0]), int(move[1]), int(move[2])

        src_stack = stacks[src_loc - 1]
        dst_stack = stacks[dst_loc - 1]

        if amount_to_move == 1:

            item_to_move = src_stack.pop(-1)
            dst_stack.append(item_to_move)
        else:
            items_to_move = src_stack[(len(src_stack)-amount_to_move):len(src_stack)]
            # print(items_to_move, amount_to_move, src_stack)

            if len(src_stack) == amount_to_move:
                src_stack = []
            else:
                for x in range((amount_to_move * -1), 0, +1):
                    src_stack.pop(x)

            dst_stack.extend(items_to_move)

        stacks[src_loc - 1] = src_stack
        stacks[dst_loc - 1] = dst_stack

        # print(stacks, amount_to_move)


    return stacks


def detect_top_stack(stacks):
    res = ""

    for stack in stacks:
        res += stack[-1]

    return res


stack_lines = []
move_lines = []

is_move_lines = False

for line in lines:
    # print(line.rstrip())

    if is_move_lines:
        move_lines.append(line.strip('\n'))
    else:
        stack_lines.append(line.strip('\n'))

    if line == "\n":
        # print("Is empty line")
        is_move_lines = True

# print("Stack lines: ", stack_lines)
# print("Move lines: ", move_lines)

stacks = tranform_stack_lines(stack_lines)
print("Stack: ", stacks)

moves = transform_move_lines(move_lines)
print("Moves: ", moves)

stacks = execute_moves(stacks, moves)
print('Resulting stacks: ', stacks)

result = detect_top_stack(stacks)
print('Result - part 2: ', result)
