def print_robots_map(robots, dimensions):
    map = [['.' for x in range(dimensions['width'])] for y in range(dimensions['height'])]
    for robot in robots:
        map[robot['y']][robot['x']] = '#'
    for row in map:
        print(''.join(row))

def calculate_movement(robots, dimensions, timeperiod):
    for robot in robots:
        totalX = robot['x'] + robot['vx'] * timeperiod
        totalY = robot['y'] + robot['vy'] * timeperiod
        remainderX = totalX % dimensions['width']
        remainderY = totalY % dimensions['height']
        lapsX = totalX // dimensions['width']
        lapsY = totalY // dimensions['height']
        robot['x'] = remainderX
        robot['y'] = remainderY
    return robots

def calculate_safety_factor(robots, dimensions):
    quadronts = {
        '1': [],
        '2': [],
        '3': [],
        '4': []
    }
    ignoreX = dimensions['width'] // 2
    ignoreY = dimensions['height'] // 2
    for robot in robots:
        if robot['x'] < ignoreX and robot['y'] < ignoreY:
            quadronts['1'].append(robot)
        elif robot['x'] > ignoreX and robot['y'] < ignoreY:
            quadronts['2'].append(robot)
        elif robot['x'] > ignoreX and robot['y'] > ignoreY:
            quadronts['3'].append(robot)
        elif robot['x'] < ignoreX and robot['y'] > ignoreY:
            quadronts['4'].append(robot)
            
    return len(quadronts['1']) * len(quadronts['2']) * len(quadronts['3']) * len(quadronts['4']) 

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
    #print_robots_map(robots, dimensions)    
    #print('-------------------')
    calculate_movement(robots, dimensions, 100)
    #print_robots_map(robots, dimensions)
    total = calculate_safety_factor(robots, dimensions)
    print(total) 