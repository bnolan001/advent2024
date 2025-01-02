scan = []
antinodes = []
merged_nodes = []


def print_map(map):
    for line in map:
        print("".join(line))

def mark_antinodes_on_line(i, j, node):
    new_nodes = 0
    for k in range(j+1, len(scan[i])):
        if scan[i][k] == node:
            x_axis = k - j
            ant_j = j - x_axis
            while ant_j >= 0:
                new_nodes += 1
                antinodes[i][ant_j] = "#"#node
                merged_nodes[i][ant_j] = "#"#node
                ant_j = ant_j - x_axis
            ant_j = k + x_axis
            while ant_j < len(scan[i]):
                new_nodes += 1
                antinodes[i][ant_j] = "#"#node
                merged_nodes[i][ant_j] = "#"#node
                ant_j = ant_j + x_axis
    return new_nodes

def mark_antinodes_later_in_scan(y, x, node):
    new_nodes = 0
    for k in range(y+1, len(scan)):
        for l in range(len(scan[k])):
            if scan[k][l] == node:
                x_axis = l - x
                y_axis = k - y
                ant_x = x - x_axis
                ant_y = y - y_axis
                while ant_x >= 0 and ant_y >= 0 and ant_x < len(scan[k]) and ant_y < len(scan):
                    new_nodes += 1
                    antinodes[ant_y][ant_x] = "#"#node
                    merged_nodes[ant_y][ant_x] = "#"#node
                    ant_x = ant_x - x_axis
                    ant_y = ant_y - y_axis
                ant_x = l + x_axis
                ant_y = k + y_axis
                while ant_x >= 0 and ant_y >= 0 and ant_x < len(scan[k]) and ant_y < len(scan):
                    new_nodes += 1
                    antinodes[ant_y][ant_x] = "#"#node
                    merged_nodes[ant_y][ant_x] = "#"#node
                    ant_x = ant_x + x_axis
                    ant_y = ant_y + y_axis
    return new_nodes
       

def find_antinodes():
    new_nodes = 0
    for i in range(len(scan)):
        for j in range(len(scan[i])):
            if scan[i][j] != ".":
                node = scan[i][j]
                # check remaining line for the same node
                new_nodes += mark_antinodes_on_line(i, j, node)
                # check for nodes down the scan
                new_nodes += mark_antinodes_later_in_scan(i, j, node)
    
    return new_nodes

def get_antinodes_count():
    total = 0
    for i in range(len(antinodes)):
        for j in range(len(antinodes[i])):
            if antinodes[i][j] != ".":
                total += 1
    return total

with open("day08/sample.txt", "r", encoding="utf8") as file:
    total = 0
    for line in file:
        if line.strip() == "":
            continue
        scan.append(list(line.strip()))
        antinodes.append(['.']*len(scan[0]))
        merged_nodes.append(list(line.strip()))

    print("------Initialized------")
    total = find_antinodes()
    get_antinodes_count()
    
    print("------Post Find Nodes------")

    print()
    print("------Original------")
    print_map(scan)
    print()
    print("------Antinodes------")
    print_map(antinodes)
    print()
    print("------Merged Notes------")
    print_map(merged_nodes)

print(total)  