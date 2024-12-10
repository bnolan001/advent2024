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
        return (-1, -1)
    
    if map[next_y][next_x] == "#":
        return get_next_move(x, y, blocked_turn[direction])
    return (next_x, next_y)

map = []
with open("day06/sample.txt", "r", encoding="utf8") as file:
    total = 0
    (x, y) = (0, 0)
    line_ct = 0
    for line in file:
        map += [list(line.strip())]
        if ('v' in map[line] or '^' in map[line] or '<' in map[line] or '>' in map[line]):
            y = line_ct
            x = map[line].index('v') if 'v' in map[line] else map[line].index('^') if '^' in map[line] else map[line].index('>') if '>' in map[line] else map[line].index('<')
        line_ct += 1

    (next_x, next_y) = (x, y) 
    while next_x != -1 and next_y != -1:
        (next_x, next_y) = get_next_move(x, y, map[y][x])
        if (next_x, next_y) != (-1, -1):
            map[y][x] = "X"
            (x, y) = (next_x, next_y)
        print_map()


print_map()
print(total)
   