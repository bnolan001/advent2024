scan = []
antinodes = []

def print_map(map):
    for line in map:
        print("".join(line))

def mark_antinodes_on_line(i, j, node):
    for k in range(j+1, len(scan[i])):
        if scan[i][k] == node:
            x_axis = k - j
            ant_j = j - x_axis
            if ant_j >= 0:
                antinodes[i][ant_j] = "#"#node
            ant_j = k + x_axis
            if ant_j < len(scan[i]):
                antinodes[i][ant_j] = "#"

def mark_antinodes_later_in_scan(y, x, node):
    for k in range(y+1, len(scan)):
        for l in range(len(scan[k])):
            if scan[k][l] == node:
                x_axis = l - x
                y_axis = k - y
                ant_x = x - x_axis
                ant_y = y - y_axis
                if ant_x >= 0 and ant_y >= 0 and ant_x < len(scan[k]) and ant_y < len(scan):
                    antinodes[ant_y][ant_x] = "#"
                ant_x = l + x_axis
                ant_y = k + y_axis
                if ant_x >= 0 and ant_y >= 0 and ant_x < len(scan[k]) and ant_y < len(scan):
                    antinodes[ant_y][ant_x] = "#"

       

def find_antinodes():
    for i in range(len(scan)):
        for j in range(len(scan[i])):
            if scan[i][j] != ".":
                node = scan[i][j]
                # check remaining line for the same node
                mark_antinodes_on_line(i, j, node)
                # check for nodes down the scan
                mark_antinodes_later_in_scan(i, j, node)
    
    return 0

def get_antinodes_count():
    total = 0
    for i in range(len(antinodes)):
        for j in range(len(antinodes[i])):
            if antinodes[i][j] != ".":
                total += 1
    return total

with open("day08/data.txt", "r", encoding="utf8") as file:
    total = 0
    for line in file:
        if line.strip() == "":
            continue
        scan.append(list(line.strip()))
        antinodes.append(['.']*len(scan[0]))
    find_antinodes()
    total = get_antinodes_count()

    print_map(scan)
    print()
    print_map(antinodes)

print(total)  # 272 is too high