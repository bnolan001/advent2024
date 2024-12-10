def print_map():
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            print(map[y][x], end="")
        print("")

map = []
with open("day06/sample.txt", "r", encoding="utf8") as file:
    total = 0
    
    for line in file:
        map += list(line.strip())

print_map()
print(total)
   