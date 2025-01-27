
def calculate_game_play(game):
    totalPlays = game["Prize"]["X"] + game["Prize"]["Y"]
    for a in range(0, game["Prize"]["X"] // game["A"]["X"]):
        for b in range(0, game["Prize"]["Y"] // game["B"]["X"]):
            xMovement = a * game["A"]["X"] + b * game["B"]["X"]
            yMovement = a * game["A"]["Y"] + b * game["B"]["Y"]
            numberOfPlays = game["Prize"]["Y"] / yMovement
            if (game["Prize"]["X"] % xMovement and
                game["Prize"]["Y"] % yMovement == 0 and
                game["Prize"]["X"] // xMovement ==
                game["Prize"]["Y"] // yMovement):
                if (numberOfPlays < totalPlays):
                    totalPlays = numberOfPlays
            totalPlays += 1
        

with open("day13/sample.txt", "r", encoding="utf8") as file:
    data = []
    total = 0
    for line in file:
        if ':' not in line:
            continue
        splitLine = line.split(' ')
        game = {}
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
    

    print(total)