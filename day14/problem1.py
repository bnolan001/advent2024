
with open("day14/sample.txt", "r", encoding="utf8") as file:
    robots = []
    total = 0
    dimensions = {"width": 101, "height": 103}
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
        

    print(total) 