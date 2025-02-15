def print_map(map):
    print('/-----------------\\')
    for row in map:
        print(''.join(row))
    
    print('\\-----------------/')

def apply_move(robot, map, move):
    next_move = robot.copy()
    movement_direction = {'x': 0, 'y': 0}
    if move == '^':
        movement_direction['y'] = -1
    elif move == 'v':
        movement_direction['y'] = 1
    elif move == '<':
        movement_direction['x'] = -1
    elif move == '>':
        movement_direction['x'] = 1

    next_move['x'] += movement_direction['x']
    next_move['y'] += movement_direction['y']
    # can't move so return current location
    if map[next_move['y']][next_move['x']] == '#':
        return robot
    # free space so move into it
    if map[next_move['y']][next_move['x']] == '.':
        return next_move
    # found an oxygen system, try to move it
    if map[next_move['y']][next_move['x']] == 'O':
        tank_check = next_move.copy()
        while True:
            if map[tank_check['y']][tank_check['x']] == '#':
                return robot
            if map[tank_check['y']][tank_check['x']] == 'O':
                tank_check['x'] += movement_direction['x']
                tank_check['y'] += movement_direction['y']
                continue
            if map[tank_check['y']][tank_check['x']] == '.':
                map[tank_check['y']][tank_check['x']] = 'O'
                map[next_move['y']][next_move['x']] = '.'
                return next_move

def drive_robot(robot, map, movement):
    for move in movement:
        map[robot['y']][robot['x']] = '.'
        robot = apply_move(robot, map, move)
        map[robot['y']][robot['x']] = '@'
        # print_map(map)
    return robot

def calculate_score(map):
    score = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'O':
                score += 100 * y + x
    return score

with open("day15/data.txt", "r", encoding="utf8") as file:
    robot = {'x': 0, 'y': 0}
    map = []
    movement = []
    total = 0

    for line in file:
        
        splitLine = list(line.strip())
        
        if len(splitLine) == 0:
            continue
        elif splitLine[0] == '#':
            map.append(splitLine)
            line_index = len(map) - 1
            if '@' in splitLine:
                robot['y'] = line_index
                robot['x'] = splitLine.index('@')
        else:
            movement += splitLine
    
    print_map(map)
    drive_robot(robot, map, movement)    
    total = calculate_score(map)
    print(total) 