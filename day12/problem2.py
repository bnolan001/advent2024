def print_map(map):
    for line in map:
        print("".join([str(x) for x in line]))
    
    print()

movement = {
    ">": {
        "x": 1,
        "y": 0,
        "next": "v"
    },
    "v": {
        "x": 0,
        "y": 1,
        "next": "<"
    },
    "<": {
        "x": -1,
        "y": 0,
        "next": "^"
    },
    "^": {
        "x": 0,
        "y": -1,
        "next": ">"
    }
}
movement_order = [">", "v", "<", "^"]

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
    starting_point = next(iter(border))
    for point in border:
        if starting_point[0] >= point[0] and starting_point[1] >= point[1]:
            starting_point = point

    current_point = (starting_point[0], starting_point[1])
    direction_steps = 0
    while True:
        if (current_point[0], current_point[1], direction) in visited_points:
            if direction_steps == 0:
                walls += 1
            elif direction_steps == 1 and walls % 2 == 1:
                walls -= 1
            break

        visited_points.add((current_point[0], current_point[1], direction))
        movement_order_index = movement_order.index(direction)
        next_point = (current_point[0] + movement[direction]["y"], current_point[1] + movement[direction]["x"])
        left_point = (current_point[0] + movement[movement_order[movement_order_index - 1]]["y"], current_point[1] + movement[movement_order[movement_order_index - 1]]["x"])
        
        if left_point in border:
            direction = movement_order[movement_order_index - 1]
            current_point = left_point
            walls += 1
            direction_steps = 1
        elif next_point in border:
            current_point = next_point
            direction_steps += 1
        else: 

            for i in range(1,4):
                direction_steps = 0
                next_dir_index = (movement_order_index + i) % 4
                test_point = (current_point[0] + movement[movement_order[next_dir_index]]["y"], current_point[1] + movement[movement_order[next_dir_index]]["x"])                
                walls += 1
                if test_point in border:
                    direction_steps += 1
                    direction = movement_order[next_dir_index]
                    
                    break
                
    return walls

def calculate_pricing(data):
    plant_data = []
    recorded_plants = set()
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1): 
            if (y, x) in recorded_plants:
                continue
            related_plants = set()
            border = set()
            result = map_plant_area(data, y, x, related_plants, border)
            recorded_plants.update(related_plants)
            walls = find_border_walls(related_plants)
            print("Plant: ", data[y][x], "Area: ", result[0], "Perimeter: ", result[1], "Border: ", border, "Walls: ", walls)
            plant_data.append({"plant": data[y][x], "area": result[0], "perimeter": result[1], "border": border, "walls":walls})
                    
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
        total += plant["area"] * plant["walls"]

    print(total) # 852420 is too low