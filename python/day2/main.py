

# f = open("test_input.txt", "r")
f = open("input.txt", "r")

lines = f.readlines()

left_column = [('A', 'Rock'), ('B', 'Paper'), ('C', 'Scissors')]
right_column = [('X', 'Rock'), ('Y', 'Paper'), ('Z', 'Scissors')]

poggers = [('X', 'Lose'), ('Y', 'Draw'), ('Z', 'Win')]

options_scores = [('Rock', 1), ('Paper', 2), ('Scissors', 3)]
match_scores = [('Win', 6), ('Draw', 3), ('Lose', 0)]
rules = [('Rock', 'Scissors', 'Lose'), ('Scissors', 'Rock', 'Win'), ('Scissors', 'Paper', 'Lose'), ('Paper', 'Scissors', 'Win'), ('Paper', 'Rock', 'Lose'), ('Rock', 'Paper', 'Win')]
rules_part_2 = [('Rock', 'Draw', 'Rock'), ('Rock', 'Lose', 'Scissors'), ('Rock', 'Win', 'Paper'), ('Paper', 'Draw', 'Paper'), ('Paper', 'Lose', 'Rock'), ('Paper', 'Win', 'Scissors'), ('Scissors','Draw','Scissors'), ('Scissors', 'Lose', 'Paper'),('Scissors','Win', 'Rock')]


def rules_part_1(opp, own):

    if opp == own:
        return "Draw"

    for rule in rules:
        if rule[0] == opp and rule[1] == own:
            return rule[2]

    return "Unknown"


def calculate_score_part_1_and_2(match_res, own_pick):
    res = 0

    for score_rule in match_scores:
        if score_rule[0] == match_res:
            res += score_rule[1]

    for score_options in options_scores:
        if score_options[0] == own_pick:
            res += score_options[1]

    return res


def what_tool_part_1(left_element, right_element):
    res_right = None
    res_left = None

    for element in left_column:
        if element[0] == left_element:
            res_left = element[1]

    for element in right_column:
        if element[0] == right_element:
            res_right = element[1]

    return res_left, res_right


def what_tool_part_2(left_element, required_match_result):
    res_right = None
    res_left = None
    required_result = None

    for element in left_column:
        if element[0] == left_element:
            res_left = element[1]

    for result in poggers:
        if result[0] == required_match_result:
            required_result = result[1]

    for rule_part_2 in rules_part_2:
        if rule_part_2[0] == res_left and rule_part_2[1] == required_result:
            res_right = rule_part_2[2]

    return res_left, res_right, required_result


total_score = 0

for line in lines:
    line_split = line.split(" ")

    left_col = line_split[0]
    right_col = line_split[1].strip('\n')

    #left, right = what_tool_part_1(left_col, right_col)
    left, right, match_result = what_tool_part_2(left_col, required_match_result=right_col)

    #match_result = rules_part_1(left, right)
    score_to_add = calculate_score_part_1_and_2(match_res=match_result, own_pick=right)

    total_score += score_to_add


print("Total Score: ", total_score)
