def print_map():
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            print(map[y][x], end="")
        print("")
    print("")

movement_config = {
    '^': {'turn':'>',
          'move_x': 0,
          'move_y': -1},
    '>': {'turn':'v',
          'move_x': 1,
          'move_y': 0},
    'v': {'turn':'<',
          'move_x': 0,
          'move_y': 1},
    '<': {'turn':'^',
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

    next_direction = map[y][x]
    map[y][x] = 'X'
    (next_x, next_y) = (x, y)
    while next_x != -1 and next_y != -1:        
        (next_x, next_y, next_direction) = get_next_move(next_x, next_y, next_direction)  
        if next_x == -1 and next_y == -1:
            continue

        map[next_y][next_x] = 'X'
       
    for line in map:
        total = line.count("X") + total

print_map()
print(total)  
   