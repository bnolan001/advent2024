# Extra sample maps from https://www.reddit.com/r/adventofcode/comments/1h94doz/i_desperately_need_help_with_day_6_part_2/

def print_map():
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            print(map[y][x], end="")
        print("")
    print("")

movement_config = {
    '^': {'turn':'>',
          'marker':'|',
          'move_x': 0,
          'move_y': -1},
    '>': {'turn':'v',
          'marker':'-',
          'move_x': 1,
          'move_y': 0},
    'v': {'turn':'<',
          'marker':'|',
          'move_x': 0,
          'move_y': 1},
    '<': {'turn':'^',
          'marker':'-',
          'move_x': -1,
          'move_y': 0}
}

def get_next_move(x, y, direction):
    next_x = x
    next_y = y
    (next_x, next_y) = (x + movement_config[direction]['move_x'], y + movement_config[direction]['move_y'])
    
    if next_x < 0 or next_x >= max_x or next_y < 0 or next_y >= max_y:
        return (-1, -1, 'O')
    
    if map[next_y][next_x] == "#":
        return get_next_move(x, y, movement_config[direction]['turn'])

    return (next_x, next_y, direction)

def can_loop_brute_force(x, y, direction):
    check_x = x + movement_config[direction]['move_x']
    check_y = y + movement_config[direction]['move_y']
    # ignore out of bounds, or areas the guard has already walked
    if (check_x < 0 or check_y < 0  or check_y >= max_y or check_x >= max_x or map[check_y][check_x] not in ['.']):
        return False

    # simulate a blockage placed on the next move
    (next_x, next_y, next_direction) = get_next_move(x, y, movement_config[direction]['turn'])
    visited = set()
    
    while(next_x != -1 and next_y != -1):
        if (next_x == x and next_y == y) or ((next_x, next_y, next_direction) in visited):
            return True
        
        visited.add((next_x, next_y, next_direction))

        (next_x, next_y, next_direction) = get_next_move(next_x, next_y, next_direction)

    return False

def mark_the_map():  
    if (prev_direction != next_direction):
        map[next_y][next_x] = movement_config[next_direction]['marker']
        map[prev_y][prev_x] = '+'
    elif (map[next_y][next_x] == '.'):
        map[next_y][next_x] = movement_config[next_direction]['marker']
    elif (map[next_y][next_x] != movement_config[next_direction]['marker']):
        map[next_y][next_x] = '+'
    else:
        map[next_y][next_x] = movement_config[next_direction]['marker']


map = []
max_x = 0
max_y = 0
with open("day06/data.txt", "r", encoding="utf8") as file:
    total = 0
    (x, y) = (0, 0)
    line_ct = 0
    for line in file:
        map += [list(line.strip())]
        if ('v' in map[line_ct] or '^' in map[line_ct] or '<' in map[line_ct] or '>' in map[line_ct]):
            y = line_ct
            x = map[line_ct].index('v') if 'v' in map[line_ct] else map[line_ct].index('^') if '^' in map[line_ct] else map[line_ct].index('>') if '>' in map[line_ct] else map[line_ct].index('<')
        line_ct += 1

    max_x = len(map[0])
    max_y = len(map)
    max_loop_steps = max_x * max_y
    direction = map[y][x]
    prev_direction = direction
    next_direction = direction
    (next_x, next_y) = (x, y)
    (prev_x, prev_y) = (x, y)
    unique_step_count = 1
    blockages = set()
    while next_x != -1 and next_y != -1:
        (block_x, block_y) = (next_x + movement_config[next_direction]['move_x'], next_y + movement_config[next_direction]['move_y'])
        if ((block_x, block_y) not in blockages and can_loop_brute_force(next_x, next_y, next_direction)):
            # Ignore walls and starting position
            if (map[block_y][block_x] not in [direction, '#']):
                blockages.add((block_x, block_y))

            print("\nStep: ", unique_step_count, "Blockages: ", len(blockages))

            #print_map()

        (prev_x, prev_y, prev_direction) = (next_x, next_y, next_direction)
        (next_x, next_y, next_direction) = get_next_move(prev_x, prev_y, prev_direction) 
        
        if next_x == -1 or next_y == -1:
            continue
        if map[next_y][next_x] == '.':
            unique_step_count += 1    

        mark_the_map()
        

print("--Completed--")
for blockage in blockages:
    map[blockage[1]][blockage[0]] = 'O'

print_map()
print(len(blockages))  # 834, 1793, 1897 is too low, 1962 is too high

   