import re

def build_operations(equation):
    actions = ['+', '*']
    operations = [] * (len(equation) - 1)
    
    total_checks = len(actions) ** (len(equation) - 2)
    for current_power in range(1, len(equation) - 1):
        pair_actions = []
        ct = 1
        action_index = 0
        current_action = actions[action_index]
        for i in range(total_checks):
            if ct > (len(actions) ** current_power / 2):
                ct = 1
                action_index += 1
                if action_index == 2:
                    action_index = 0
                current_action = actions[action_index]
            pair_actions.append(current_action)
            ct += 1
        operations.append(pair_actions)

    return operations

def is_valid(equation, operations):
    for i in range(len(operations[0])):
        value = equation[1]
        for j in range(len(equation) - 2):
            if operations[j][i] == '+':
                value = value + equation[j + 2]
            else:
                value = value * equation[j + 2]
                
        if value == equation[0]:
            return True
    return False

def check_equations():
    total = 0
    for equation in equations:
        operations = build_operations(equation)
        if is_valid(equation, operations):
            print("Valid", equation)
            total += equation[0]
    return total

equations = []
with open("day07/data.txt", "r", encoding="utf8") as file:
    total = 0
    for line in file:
        if line.strip() == "":
            continue
        values = re.split(':| ', line.strip())
        values.remove('')
        equations.append([int(item) for item in values])
    
    total = check_equations()

print(total)  
   