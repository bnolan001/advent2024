def print_map(map):
    for line in map:
        print("".join([str(x) for x in line]))

with open("day10/sample.txt", "r", encoding="utf8") as file:
    map = []
    total = 0
    for line in file:
        map.append(list([int(x) for x in line.strip()]))

    print(map)
    print_map(map)
    print(total)