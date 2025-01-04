scan = []
antinodes = []
merged_nodes = []


def print_map(map):
    for line in map:
        print("".join(line))

def mark_antinodes_vertically(y, x, node, main_map):
    for k in range(y+1, len(main_map)):
        for l in range(len(main_map[k])):
            if main_map[k][l] == node:
                x_axis = l - x
                y_axis = k - y
                ant_x = x - x_axis
                ant_y = y - y_axis
                antinodes[y][x] = node
                antinodes[k][l] = node
                while ant_x >= 0 and ant_y >= 0 and ant_x < len(main_map[k]) and ant_y < len(main_map):
                    antinodes[ant_y][ant_x] = node
                    merged_nodes[ant_y][ant_x] = node
                    ant_x = ant_x - x_axis
                    ant_y = ant_y - y_axis
                ant_x = l + x_axis
                ant_y = k + y_axis
                while ant_x >= 0 and ant_y >= 0 and ant_x < len(main_map[k]) and ant_y < len(main_map):
                    antinodes[ant_y][ant_x] = node
                    merged_nodes[ant_y][ant_x] = node
                    ant_x = ant_x + x_axis
                    ant_y = ant_y + y_axis
       

def find_antinodes(main_map):
    for y in range(len(main_map)):
        for x in range(len(main_map[y])):
            if main_map[y][x] != ".":
                node = main_map[y][x]
                mark_antinodes_vertically(y, x, node, main_map)
    

def get_antinodes_count():
    total = 0
    for y in range(len(antinodes)):
        total += len(antinodes[y]) - antinodes[y].count(".")

    return total

with open("day08/data.txt", "r", encoding="utf8") as file:
    total = 0
    for line in file:
        if line.strip() == "":
            continue
        scan.append(list(line.strip()))
        antinodes.append(['.']*len(scan[0]))
        merged_nodes.append(list(line.strip()))

    find_antinodes(scan)
    total = get_antinodes_count()   
    print(total)

