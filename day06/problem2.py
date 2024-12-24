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

map = []
with open("day06/sample.txt", "r", encoding="utf8") as file:
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
    map[y][x] = movement_config[direction]['marker']
    prev_direction = direction
    (prev_x, prev_y) = (x, y)
    (next_x, next_y, next_direction) = get_next_move(x, y, direction)
    while next_x != -1 and next_y != -1:        
        (next_x, next_y, next_direction) = get_next_move(next_x, next_y, next_direction)  
        if next_x == -1 and next_y == -1:
            continue

        if (prev_direction != next_direction) or (map[next_y][next_x] == movement_config[next_direction]['marker']):
            map[prev_y][prev_x] = '+'
        elif (map[next_y][next_x] == '.'):
            map[next_y][next_x] = movement_config[next_direction]['marker']
        else:
            map[next_y][next_x] = movement_config[next_direction]['marker']
        prev_direction = next_direction

        print_map()
       
    for line in map:
        total = line.count("O") + total

print_map()
print(total)
   