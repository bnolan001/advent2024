scan = []
antinodes = []
merged_nodes = []


def print_map(map):
    for line in map:
        print("".join(line))

def mark_antinodes_on_line(i, j, node, main_map):
    new_nodes = 0
    for k in range(j+1, len(main_map[i])):
        if main_map[i][k] == node:
            x_axis = k - j
            ant_j = j - x_axis
            while ant_j >= 0:
                new_nodes += 1
                antinodes[i][ant_j] = node
                merged_nodes[i][ant_j] = node
                ant_j = ant_j - x_axis
            ant_j = k + x_axis
            while ant_j < len(main_map[i]):
                new_nodes += 1
                antinodes[i][ant_j] = node
                merged_nodes[i][ant_j] = node
                ant_j = ant_j + x_axis
    return new_nodes

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
                # check remaining line for the same node
                #mark_antinodes_on_line(y, x, node, main_map)
                # check for nodes down the scan
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

    print("------Original Scan------")
    print_map(scan)
    find_antinodes(scan)
    print("------Post Find Antinodes------")
    print_map(antinodes)
    total = get_antinodes_count()
    print("------Antinodes Count------")
    print(total)
    print()
    # print("------Post Find Merged second------")
    # print_map(merged_nodes)
    
    # print()
    # total = find_antinodes(merged_nodes)
    # print("------Post Find Antinodes second run------")
    # print_map(antinodes)
    # print("------Post Find Merged second run------")
    # print_map(merged_nodes)
    # print()
    # print("------Antinodes Count second run------")
    # print(total)
    # print("------Post Find Nodes------")

    # print()
    # print("------Original------")
    # print_map(scan)
    # print()
    # print("------Antinodes------")
    # print_map(antinodes)
    # print()
    # print("------Merged Notes------")
    # print_map(merged_nodes)

