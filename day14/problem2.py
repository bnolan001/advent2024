def get_robot_map(robots, dimensions):
    map = [['.' for x in range(dimensions['width'])] for y in range(dimensions['height'])]
    for robot in robots:
        map[robot['y']][robot['x']] = '#'
    return map

def print_robots_map(robots, dimensions):
    map = get_robot_map(robots, dimensions)
    with open("day14/data_output.txt", "a") as file:
        
        for row in map:
            file.write(''.join(row))
            file.write('\n')
        file.write('\n')


def check_for_tree(robots, dimensions):
    # After running the simulation, check if there are at least two borders in the map
    # if there are then there is most likely a tree on this map
    top_bottom_border = '###############################'
    border_count = 0
    for row in get_robot_map(robots, dimensions):
        row_string = ''.join(row)
        if top_bottom_border in row_string:
            border_count += 1
    
    if border_count >= 2:
        return True

def calculate_movement(robots, dimensions):
    for robot in robots:
        totalX = (robot['x'] + robot['vx']) % dimensions['width']
        totalY = (robot['y'] + robot['vy']) % dimensions['height']
        
        robot['x'] = totalX
        robot['y'] = totalY
    return robots

def find_christmas_tree(robots, dimensions):
    for x in range(10000):
        calculate_movement(robots, dimensions)
        if check_for_tree(robots, dimensions):
            return x + 1
            
robots = []
total = 0
dimensions = {"width": 101, "height": 103} # data.txt
#dimensions = {"width": 11, "height": 7} # sample.txt      

with open("day14/data.txt", "r", encoding="utf8") as file:
    for line in file:
        splitLine = line.replace('p=', '').replace('v=', '').split(' ')
        startingPoint = splitLine[0].split(',')
        velocity = splitLine[1].split(',')
        robots.append({
            'x': int(startingPoint[0]),
            'y': int(startingPoint[1]),
            'vx': int(velocity[0]),
            'vy': int(velocity[1])
        })

total = find_christmas_tree(robots, dimensions)
    
print(total) 