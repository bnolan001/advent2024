def euclidean_algorithm(a, b):
    if a < b:
        (a,b) = (b,a)

    if b == 0:
        return a
    return euclidean_algorithm(b, a % b)



def calculate_game_button_presses(game):
    buttonPresses = {"A": 0, "B": 0}
    
    a = abs((game["Prize"]["X"] * game["B"]["Y"] - game["Prize"]["Y"] * game["B"]["X"]) / 
            (game["A"]["X"] * game["B"]["Y"] - game["A"]["Y"] * game["B"]["X"]))
    b = abs((game["Prize"]["X"] * game["A"]["Y"] - game["Prize"]["Y"] * game["A"]["X"]) / 
            (game["A"]["X"] * game["B"]["Y"] - game["A"]["Y"] * game["B"]["X"]))
    
    if (a.is_integer() and b.is_integer()):
        buttonPresses["A"] = int(a)
        buttonPresses["B"] = int(b)
    
    return buttonPresses

def process_games(data):
    totalPlays = []
    for game in data:
        
        result = calculate_game_button_presses(game)
        totalPlays.append(result)
        print("Game", len(totalPlays), "requires", totalPlays[-1]["A"], "presses of button A and", totalPlays[-1]["B"], "presses of button B")

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