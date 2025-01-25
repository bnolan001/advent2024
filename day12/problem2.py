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

def count_corners(related_plants):
    starting_point = next(iter(related_plants))
    for point in related_plants:
        if starting_point[0] >= point[0] and starting_point[1] >= point[1]:
            starting_point = point
    corners = 0
    for point in related_plants:
        left_point = (point[0], point[1] - 1)
        right_point = (point[0], point[1] + 1)
        upper_point = (point[0] - 1, point[1])
        down_point = (point[0] + 1, point[1])
        upper_left_point = (point[0] - 1, point[1] - 1)
        upper_right_point = (point[0] - 1, point[1] + 1)
        down_left_point = (point[0] + 1, point[1] - 1)
        down_right_point = (point[0] + 1, point[1] + 1)

        ### Ouside Corners
        #  X
        # XA
        if (upper_point not in related_plants and 
            left_point not in related_plants):
            corners += 1

        # X
        # AX
        if (upper_point not in related_plants and 
            right_point not in related_plants):
            corners += 1

        # XA
        #  X
        if (down_point not in related_plants and 
            left_point not in related_plants):
            corners += 1

        # AX
        # X
        if (down_point not in related_plants and 
            right_point not in related_plants):
            corners += 1

        ### Inside Corners
        # aX
        # aA
        if (upper_left_point in related_plants and 
            left_point in related_plants and
            upper_point not in related_plants):
            corners += 1
        
        # Xa
        # Aa
        if (upper_right_point in related_plants and 
            right_point in related_plants and
            upper_point not in related_plants):
            corners += 1
        
        # aA
        # aX
        if (down_left_point in related_plants and 
            left_point in related_plants and
            down_point not in related_plants):
            corners += 1
        
        # Aa
        # Xa
        if (down_right_point in related_plants and 
            right_point in related_plants and
            down_point not in related_plants):
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
            result = map_plant_area(data, y, x, related_plants)
            recorded_plants.update(related_plants)
            corners = count_corners(related_plants, data)
            plant_data.append({"plant": data[y][x], "area": result[0], "perimeter": result[1], "corners": corners})
                    
    return plant_data

with open("day12/data.txt", "r", encoding="utf8") as file:
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

    print(total) 