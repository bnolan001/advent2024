def euclidean_algorithm(a, b):
    if a < b:
        (a,b) = (b,a)

    if b == 0:
        return a
    return euclidean_algorithm(b, a % b)



def calculate_game_button_presses(game):
    buttonPresses = {"A": 0, "B": 0}
    
    minX = min(game["A"]["X"], game["B"]["X"])
    for a in range(0, game["Prize"]["X"] // minX + 1):
        remainingX = game["Prize"]["X"] - game["A"]["X"] * a
        remainingY = game["Prize"]["Y"] - game["A"]["Y"] * a
        if (remainingX % game["B"]["X"] != 0 or remainingY % game["B"]["Y"] != 0 or 
            remainingX // game["B"]["X"] != remainingY // game["B"]["Y"]):
            continue
       
        b = remainingY // game["B"]["Y"]
        
        buttonPresses["A"] = a
        buttonPresses["B"] = b
        break
    return buttonPresses

def process_games(data):
    totalPlays = []
    for game in data:
        gcmX = euclidean_algorithm(game["A"]["X"], game["B"]["X"])
        gcmY = euclidean_algorithm(game["A"]["Y"], game["B"]["Y"])
        if gcmX == 1 or gcmY == 1:
            print("Skipping")
            continue
        print("GCM X", gcmX, "GCM Y", gcmY)
        #totalPlays.append(calculate_game_button_presses(game))
        #print("Game", len(totalPlays), "requires", totalPlays[-1]["A"], "presses of button A and", totalPlays[-1]["B"], "presses of button B")

    return totalPlays

with open("day13/data.txt", "r", encoding="utf8") as file:
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
            x = int(splitLine[1].split('=')[1].replace(',', '')) + 10000000000000
            y = int(splitLine[2].split('=')[1]) + 10000000000000
            game["Prize"] = {"X": x, "Y": y}
            data.append(game)
        
    
    gampe_play = process_games(data)
    for game in gampe_play:
        total += game["A"]  * 3+ game["B"] 

    print(total) 