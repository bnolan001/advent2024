def print_map(map):
    for line in map:
        print("".join([str(x) for x in line]))
    
    print()

def map_plant_area(data, y, x, recorded_plants):
    plant = data[y][x]
    recorded_plants.add((y, x))
    perimeter = 0
    area = 1
    if (y + 1, x) not in recorded_plants:
        if data[y + 1][x] != plant:
            perimeter += 1
        else:
            #area += 1
            result = map_plant_area(data, y + 1, x, recorded_plants)
            area += result[0]
            perimeter += result[1]

    if (y - 1, x) not in recorded_plants:
        if data[y - 1][x] != plant:
            perimeter += 1
        else:
            #area += 1
            result = map_plant_area(data, y - 1, x, recorded_plants)
            area += result[0]
            perimeter += result[1]

    if (y, x + 1) not in recorded_plants:        
        if data[y][x + 1] != plant:
            perimeter += 1
        else:
            #area += 1
            result = map_plant_area(data, y, x + 1, recorded_plants)
            area += result[0]
            perimeter += result[1]
    
    if (y, x - 1) not in recorded_plants:
        if data[y][x - 1] != plant:
            perimeter += 1
        else:
            #area += 1
            result = map_plant_area(data, y, x - 1, recorded_plants)
            area += result[0]
            perimeter += result[1]

    return (area, perimeter)

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
            plant_data.append({"plant": data[y][x], "area": result[0], "perimeter": result[1]})
                    
    
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
    print("Distinct plants", distinct_plants)
    data.append(['*'] * (len(line) + 1))
    print_map(data)
    
    plant_data = calculate_pricing(data)

    print(plant_data)

    for plant in plant_data:
        total += plant["area"] * plant["perimeter"]

    print(total)