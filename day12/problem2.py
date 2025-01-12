def print_map(map):
    for line in map:
        print("".join([str(x) for x in line]))
    
    print()

def map_plant_area(data, y, x, recorded_plants, plant_perimeters):
    plant = data[y][x]
    recorded_plants.add((y, x))
    perimeter = 0
    area = 1
    if (y + 1, x) not in recorded_plants:
        if data[y + 1][x] != plant:
            perimeter += 1
            plant_perimeters.add((y,x))
        else:
            result = map_plant_area(data, y + 1, x, recorded_plants, plant_perimeters)
            area += result[0]
            perimeter += result[1]

    if (y - 1, x) not in recorded_plants:
        if data[y - 1][x] != plant:
            perimeter += 1
            plant_perimeters.add((y,x))
        else:
            result = map_plant_area(data, y - 1, x, recorded_plants, plant_perimeters)
            area += result[0]
            perimeter += result[1]

    if (y, x + 1) not in recorded_plants:        
        if data[y][x + 1] != plant:
            perimeter += 1
            plant_perimeters.add((y,x))
        else:
            result = map_plant_area(data, y, x + 1, recorded_plants, plant_perimeters)
            area += result[0]
            perimeter += result[1]
    
    if (y, x - 1) not in recorded_plants:
        if data[y][x - 1] != plant:
            perimeter += 1
            plant_perimeters.add((y,x))
        else:
            result = map_plant_area(data, y, x - 1, recorded_plants, plant_perimeters)
            area += result[0]
            perimeter += result[1]

    return (area, perimeter)

def calculate_pricing(data):
    plant_data = []
    perimeters = []
    recorded_plants = set()
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1): 
            if (y, x) in recorded_plants:
                continue
            related_plants = set()
            plant_perimeters = set()
            result = map_plant_area(data, y, x, related_plants, plant_perimeters)
            recorded_plants.update(related_plants)
            plant_data.append({"plant": data[y][x], "area": result[0], "perimeter": result[1]})
            perimeters.append({"plant": data[y][x], "plant_perimeter": plant_perimeters})
                    
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