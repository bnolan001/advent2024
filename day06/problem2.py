def print_map():
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            print(map[y][x], end="")
        print("")
    print("")

blocked_turn = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
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
        return get_next_move(x, y, blocked_turn[direction])
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

    (next_x, next_y) = (x, y) 
    direction = map[y][x]
    while next_x != -1 and next_y != -1:
        map[next_y][next_x] = direction
        (next_x, next_y, direction) = get_next_move(x, y, map[y][x])
        if (next_x, next_y) != (-1, -1):
            if map[next_y][next_x] != ".":
                (temp_x, temp_y, temp_direction) = get_next_move(next_x, next_y, blocked_turn[direction])
                if (temp_x, temp_y) != (-1, -1) and map[temp_y][temp_x] != ".":
                    map[next_y][next_x] = "O"
            map[y][x] = "X"
            (x, y) = (next_x, next_y)
        print_map()
       
    for line in map:
        total = line.count("O") + total

print_map()
print(total)
   