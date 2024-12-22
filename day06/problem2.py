def print_map():
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            print(map[y][x], end="")
        print("")
    print("")

blocked_turn = {
    '^': {'turn':'>',
          'marker':'|'},
    '>': {'turn':'v',
          'marker':'-'},
    'v': {'turn':'<',
          'marker':'|'},
    '<': {'turn':'^',
          'marker':'-'}
}

def get_next_move(x, y, direction):
    next_x = x
    next_y = y
    if direction == "^":
        (next_x, next_y) = (x, y - 1)
    elif direction == "v":
        (next_x, next_y) = (x, y + 1)
    elif direction == "<":
        (next_x, next_y) = (x - 1, y)
    elif direction == ">":
        (next_x, next_y) = (x + 1, y)
    if next_x < 0 or next_x >= len(map[0]) or next_y < 0 or next_y >= len(map):
        return (-1, -1, 'O')
    
    if map[next_y][next_x] == "#":
        return get_next_move(x, y, blocked_turn[direction]['turn'])
    return (next_x, next_y, direction)

def is_next_move_blocked(x, y, direction):
    (next_x, next_y, next_direction) = get_next_move(x, y, direction)
    if (direction != next_direction):
        return True
    
    if (map[next_y][next_x] == "O"):
        return True
    
    return False


def walk_the_map(x, y, direction):
    if (map[y][x] == "O"):
        return
    if (map[y][x] == "."):
        map[y][x] = "X"
        return
    if (map[y][x] == "X"):
        if (is_next_move_blocked(x, y, direction) == False):
            map[y][x] = "O"
            return

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
    map[y][x] = "X"
    prev_direction = direction
    (next_x, next_y, next_direction) = get_next_move(x, y, direction)
    while next_x != -1 and next_y != -1:
        
        walk_the_map(next_x, next_y, next_direction)
        
        (next_x, next_y, next_direction) = get_next_move(next_x, next_y, next_direction)  
        if (prev_direction != next_direction):
            map[next_y][next_x] = '+'
        else:            
            map[next_y][next_x] = blocked_turn[prev_direction]['marker']      
        prev_direction = next_direction

        print_map()
       
    for line in map:
        total = line.count("O") + total

print_map()
print(total)
   