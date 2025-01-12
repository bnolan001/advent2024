def print_map(map):
    for line in map:
        print("".join([str(x) for x in line]))
    
    print()

def map_plant_area(data, y, x, recorded_plants, border):
    plant = data[y][x]
    recorded_plants.add((y, x))
    perimeter = 0
    area = 1
    if (y + 1, x) not in recorded_plants:
        if data[y + 1][x] != plant:
            perimeter += 1
            border.add((y,x))
        else:
            result = map_plant_area(data, y + 1, x, recorded_plants, border)
            area += result[0]
            perimeter += result[1]

    if (y - 1, x) not in recorded_plants:
        if data[y - 1][x] != plant:
            perimeter += 1
            border.add((y,x))
        else:
            result = map_plant_area(data, y - 1, x, recorded_plants, border)
            area += result[0]
            perimeter += result[1]

    if (y, x + 1) not in recorded_plants:        
        if data[y][x + 1] != plant:
            perimeter += 1
            border.add((y,x))
        else:
            result = map_plant_area(data, y, x + 1, recorded_plants, border)
            area += result[0]
            perimeter += result[1]
    
    if (y, x - 1) not in recorded_plants:
        if data[y][x - 1] != plant:
            perimeter += 1
            border.add((y,x))
        else:
            result = map_plant_area(data, y, x - 1, recorded_plants, border)
            area += result[0]
            perimeter += result[1]

    return (area, perimeter)

def find_border_walls(border):
    walls = 0
    visited_points = set()
    direction = '>'
    starting_point = border[0]
    for point in border:
        if starting_point > point:
            starting_point = point

    visited_points.add((starting_point[0], starting_point[1], direction))
    current_point = (starting_point[0], starting_point[1])
    while True:
        if direction == '>':
            next_point = (current_point[0], current_point[1] + 1)
        elif direction == '<':
            next_point = (current_point[0], current_point[1] - 1)
        elif direction == '^':
            next_point = (current_point[0] - 1, current_point[1])
        elif direction == 'v':
            next_point = (current_point[0] + 1, current_point[1])

        if (next_point[0], next_point[1], direction) in visited_points:
            break

        visited_points.add((current_point[0], current_point[1], direction))
        if next_point in border:
            current_point = next_point
        else:            
            walls += 1
            if direction == '>':
                direction = 'v'
            elif direction == 'v':
                direction = '<'
            elif direction == '<':
                direction = '^'
            elif direction == '^':
                direction = '>'
    return walls

def calculate_pricing(data):
    plant_data = []
    perimeters = []
    recorded_plants = set()
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1): 
            if (y, x) in recorded_plants:
                continue
            related_plants = set()
            border = set()
            result = map_plant_area(data, y, x, related_plants, border)
            recorded_plants.update(related_plants)
            walls = find_border_walls(border)
            plant_data.append({"plant": data[y][x], "area": result[0], "perimeter": result[1], "border": border, "walls":walls})
                    
    print(perimeters)
    return plant_data

with open("day12/sample.txt", "r", encoding="utf8") as file:
    data = []
    distinct_plants = {"*"}
    total = 0
    for line in file:
        if len(data) == 0:
            data.append(['*'] * (len(line) + 1))
        data.append(['*'] + list(line.strip()) + ['*'])
        distinct_plants.update(data[len(data) - 1])

    distinct_plants.remove("*")
    data.append(['*'] * (len(data[0])))
    
    plant_data = calculate_pricing(data)

    for plant in plant_data:
        total += plant["area"] * plant["perimeter"]

    print(total)