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

def count_border_walls(border):
    walls = 0
    visited_points = set()
    direction = '>'
    starting_point = next(iter(border))
    for point in border:
        if starting_point[0] >= point[0] and starting_point[1] >= point[1]:
            starting_point = point

    current_point = (starting_point[0], starting_point[1])
    first_step = True
    while True:
        if (current_point[0], current_point[1], direction) in visited_points:
            if walls % 2 == 1:
                walls -= 1
            break

        if first_step:
            walls += 1

        visited_points.add((current_point[0], current_point[1], direction))
        movement_order_index = movement_order.index(direction)
        next_point = (current_point[0] + movement[direction]["y"], current_point[1] + movement[direction]["x"])
        left_point = (current_point[0] + movement[movement_order[movement_order_index - 1]]["y"], current_point[1] + movement[movement_order[movement_order_index - 1]]["x"])
        
        if left_point in border:
            direction = movement_order[movement_order_index - 1]
            current_point = left_point
            first_step = True
        elif next_point in border:
            current_point = next_point
            first_step = False
        else: 
            first_step = True
            for i in range(1,4):
                next_dir_index = (movement_order_index + i) % 4
                test_point = (current_point[0] + movement[movement_order[next_dir_index]]["y"], current_point[1] + movement[movement_order[next_dir_index]]["x"])                
                
                if test_point in border:
                    direction = movement_order[next_dir_index]
                    current_point = test_point
                    break
                
                walls += 1
                
    return walls

def count_corners(related_plants, map):
    starting_point = next(iter(related_plants))
    for point in related_plants:
        if starting_point[0] >= point[0] and starting_point[1] >= point[1]:
            starting_point = point
    plant = map[starting_point[0]][starting_point[1]]
    corners = 0
    for point in related_plants:
        left_point = (point[0], point[1] - 1)
        right_point = (point[0], point[1] + 1)
        upper_point = (point[0] -1, point[1])
        down_point = (point[0] + 1, point[1])
        upper_left_point = (point[0] - 1, point[1] - 1)
        upper_right_point = (point[0] - 1, point[1] + 1)
        down_left_point = (point[0] + 1, point[1] - 1)
        down_right_point = (point[0] + 1, point[1] + 1)

        if upper_point not in related_plants and left_point not in related_plants:
            corners += 1

        if upper_point not in related_plants and right_point not in related_plants:
            corners += 1

        if down_point not in related_plants and left_point not in related_plants:
            corners += 1

        if down_point not in related_plants and right_point not in related_plants:
            corners += 1
        
        if upper_left_point not in related_plants and upper_point not in related_plants:
            corners += 1
        
        if upper_right_point not in related_plants and upper_point not in related_plants:
            corners += 1
        
        if down_left_point not in related_plants and down_point not in related_plants:
            corners += 1
        
        if down_right_point not in related_plants and down_point not in related_plants:
            corners += 1

    return corners

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
            walls = count_border_walls(related_plants)
            corners = count_corners(related_plants, data)
            print("Plant: ", data[y][x], "Area: ", result[0], "Perimeter: ", result[1], "Walls: ", walls, "Corners:", corners)
            plant_data.append({"plant": data[y][x], "area": result[0], "perimeter": result[1], "border": border, "walls":walls, "corners": corners})
                    
    return plant_data

with open("day12/sample_6.txt", "r", encoding="utf8") as file:
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
        total += plant["area"] * plant["corners"]

    print(total) # 852420 is too low, 879720 is too high