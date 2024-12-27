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
    
    if next_x < 0 or next_x >= len(map[0]) or next_y < 0 or next_y >= len(map):
        return (-1, -1, 'O')
    
    if map[next_y][next_x] == "#":
        return get_next_move(x, y, movement_config[direction]['turn'])

    return (next_x, next_y, direction)

def can_loop(x, y, direction):
    turn = movement_config[direction]['turn']
    (next_x, next_y, next_direction) = get_next_move(x, y, direction)
    # there is already a blockage on the next move
    if (next_x == -1 and next_y == -1) or (direction != next_direction) or (map[next_y][next_x] != '.'):
        return False
    
    (next_x, next_y, next_direction) = get_next_move(x, y, turn)
    if(map[next_y][next_x] in ['+','|', '-']):
        return True

    return False

def can_loop_brute_force(x, y, direction):
    num_turns = 0
    # simulate a blockage placed on the next move
    (next_x, next_y, next_direction) = get_next_move(x, y, movement_config[direction]['turn'])
    if (map[next_y][next_x] == '#'):
        (next_x, next_y, next_direction) = get_next_move(x, y, movement_config[movement_config[direction]['turn']])

    current_direction = next_direction
    while(next_x != -1 and next_y != -1) and num_turns < 4:
        if (next_x == x and next_y == y):
            return True
        if (current_direction != next_direction):
            num_turns += 1
            current_direction = next_direction
        (next_x, next_y, next_direction) = get_next_move(next_x, next_y, next_direction)

    return False

map = []
with open("day06/sample_3.txt", "r", encoding="utf8") as file:
    total = 0
    (x, y) = (0, 0)
    line_ct = 0
    for line in file:
        map += [list(line.strip())]
        if ('v' in map[line_ct] or '^' in map[line_ct] or '<' in map[line_ct] or '>' in map[line_ct]):
            y = line_ct
            x = map[line_ct].index('v') if 'v' in map[line_ct] else map[line_ct].index('^') if '^' in map[line_ct] else map[line_ct].index('>') if '>' in map[line_ct] else map[line_ct].index('<')
        line_ct += 1

    direction = map[y][x]
    map[y][x] = direction
    prev_direction = direction
    (next_x, next_y) = (x, y)
    (prev_x, prev_y) = (x, y)
    unique_step_count = 1
    while next_x != -1 and next_y != -1:        
        (next_x, next_y, next_direction) = get_next_move(prev_x, prev_y, prev_direction)  
        if next_x == -1 and next_y == -1:
            continue

        if map[next_y][next_x] == '.':
            unique_step_count += 1

        if (map[next_y][next_x] == direction) or (map[next_y][next_x] == 'O'):
            (prev_x, prev_y, prev_direction) = (next_x, next_y, next_direction)
            continue
        if (prev_direction != next_direction):
            map[next_y][next_x] = movement_config[next_direction]['marker']
            map[prev_y][prev_x] = '+'
        elif (map[next_y][next_x] == '.'):
            map[next_y][next_x] = movement_config[next_direction]['marker']
        elif (map[next_y][next_x] != movement_config[next_direction]['marker']):
            map[next_y][next_x] = '+'
        else:
            map[next_y][next_x] = movement_config[next_direction]['marker']
        (prev_x, prev_y, prev_direction) = (next_x, next_y, next_direction)

        if (can_loop_brute_force(next_x, next_y, next_direction)):
            (block_x, block_y, block_direction) = get_next_move(next_x, next_y, next_direction)
            map[block_y][block_x] = 'O'

        print("\nStep: ", unique_step_count)
        print_map()
       
    for line in map:
        total = line.count("O") + total
print("--Completed--")
print_map()
print(total)  # 834 is too low
   