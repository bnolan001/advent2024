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
    print_robots_map(robots, dimensions)    
    print('-------------------')
    calculate_movement(robots, dimensions, 100)
    print_robots_map(robots, dimensions)
    print(total) 