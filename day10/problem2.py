def print_map(map):
    for line in map:
        print("".join([str(x) for x in line]))
    
    print()

def traverse_paths(map, x, y, path):
    total = 0
    point_value = map[y][x]
    if point_value == 9:
        path[y][x] = point_value
        #print_map(path)
        path[y][x] = '#'
        return 1
    
    next_point = point_value + 1  
    if y > 0 and map[y - 1][x] == next_point:
        path[y][x] = point_value
        total += traverse_paths(map, x, y - 1, path)
        path[y][x] = '#'
    if y < len(map) - 1 and map[y + 1][x] == next_point:
        path[y][x] = point_value
        total += traverse_paths(map, x, y + 1, path)
        path[y][x] = '#'
    if x > 0 and map[y][x - 1] == next_point:
        path[y][x] = point_value
        total += traverse_paths(map, x - 1, y, path)
        path[y][x] = '#'
    if x < len(map[y]) - 1 and map[y][x + 1] == next_point:
        path[y][x] = point_value
        total += traverse_paths(map, x + 1, y, path)
        path[y][x] = '#'
    
    return total

def count_paths(map):
    total = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                path = [['#' for _ in range(len(map[y]))] for _ in range(len(map))]
                total += traverse_paths(map, x, y, path)
    
    return total

with open("day10/data.txt", "r", encoding="utf8") as file:
    map = []
    total = 0
    for line in file:
        map.append(list([int(x) for x in line.strip()]))

    total = count_paths(map)
    #print_map(map)
    print(total)