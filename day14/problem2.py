def print_robots_map(robots, dimensions):
    map = [['.' for x in range(dimensions['width'])] for y in range(dimensions['height'])]
    for robot in robots:
        map[robot['y']][robot['x']] = '#'
    for row in map:
        print(''.join(row))

def check_for_tree(robots, dimensions):
    center_point = dimensions['width'] // 2
    height = center_point + 2
    top = {}
    bottom = {}
    for robot in robots:
        if robot['x'] == center_point and robot['y'] == 0:
            top = robot
        if robot['x'] == center_point and robot['y'] == height:
            bottom = robot

    if top and bottom:
        return True

def calculate_movement(robots, dimensions):
    for robot in robots:
        totalX = (robot['x'] + robot['vx']) % dimensions['width']
        totalY = (robot['y'] + robot['vy']) % dimensions['height']
        
        robot['x'] = totalX
        robot['y'] = totalY
    return robots

def find_christmas_tree(robots, dimensions):
    for x in range(10000000):
        calculate_movement(robots, dimensions)
        if check_for_tree(robots, dimensions):
            print_robots_map(robots, dimensions)
            print('-------------------')
            
        

with open("day14/sample.txt", "r", encoding="utf8") as file:
    robots = []
    total = 0
    # dimensions = {"width": 101, "height": 103} # data.txt
    dimensions = {"width": 11, "height": 7} # sample.txt

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
    find_christmas_tree(robots, dimensions)
    #print_robots_map(robots, dimensions)
    
    print(total) 