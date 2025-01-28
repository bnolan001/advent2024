
def calculate_game_button_presses(game):
    buttonPresses = {}
    minCost = 100000000000
    minX = min(game["A"]["X"], game["B"]["X"])
    minY = min(game["A"]["Y"], game["B"]["Y"])
    for a in range(0, game["Prize"]["X"] // minX + 1):
        for b in range(0, game["Prize"]["Y"] // minY + 1):
            if (a * 1 + b * 3 > minCost):
                continue

            xMovement = a * game["A"]["X"] + b * game["B"]["X"]
            yMovement = a * game["A"]["Y"] + b * game["B"]["Y"]
            playCost = a * 1+ b * 3
            if (game["Prize"]["X"] == xMovement and
                game["Prize"]["Y"] == yMovement):
                if (playCost < minCost):
                    buttonPresses["A"] = a
                    buttonPresses["B"] = b
                    minCost = playCost
    return buttonPresses

def process_games(data):
    totalPlays = []
    for game in data:
        totalPlays.append(calculate_game_button_presses(game))
    print(totalPlays)
    return totalPlays

with open("day13/sample.txt", "r", encoding="utf8") as file:
    data = []
    total = 0
    game = {}
    for line in file:
        if ':' not in line:
            game = {}
            continue
        splitLine = line.split(' ')
        
        if "A" in splitLine[1]:
            x = int(splitLine[2].split('+')[1].replace(',', ''))
            y = int(splitLine[3].split('+')[1])
            game["A"] = {"X": x, "Y": y}
        elif "B" in splitLine[1]:
            x = int(splitLine[2].split('+')[1].replace(',', ''))
            y = int(splitLine[3].split('+')[1])
            game["B"] = {"X": x, "Y": y}
        elif "Prize" in splitLine[0]:
            x = int(splitLine[1].split('=')[1].replace(',', ''))
            y = int(splitLine[2].split('=')[1])
            game["Prize"] = {"X": x, "Y": y}
            data.append(game)
        
    
    process_games(data)
    

    print(total)