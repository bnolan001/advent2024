
def calculate_game_button_presses(game):
    buttonPresses = {}
    minCost = 100000000000
    for a in range(0, game["Prize"]["X"] // game["A"]["X"]):
        for b in range(0, game["Prize"]["Y"] // game["B"]["X"]):
            if (a == 0 and b == 0 or
                a == 0 and b > 1):
                continue

            xMovement = a * game["A"]["X"] + b * game["B"]["X"]
            yMovement = a * game["A"]["Y"] + b * game["B"]["Y"]
            playCost = a * 1+ b * 3
            if (game["Prize"]["X"] == xMovement and
                game["Prize"]["Y"] == yMovement):
                if (playCost < minCost):
                    buttonPresses["A"] = a
                    buttonPresses["B"] = b
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
        
    print(data)
    process_games(data)
    

    print(total)