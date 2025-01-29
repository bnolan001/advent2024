
def calculate_game_button_presses(game):
    ''' Calculate the number of required moves by Cramer's Rule '''
    # https://byjus.com/maths/cramers-rule/#:~:text=In%20linear%20algebra%2C%20Cramer%E2%80%99s%20rule%20is%20a%20specific,the%20system%20of%20equations%20has%20a%20unique%20solution.
    # https://www.reddit.com/r/adventofcode/comments/1hd7irq/2024_day_13_an_explanation_of_the_mathematics/
    buttonPresses = {"A": 0, "B": 0}
    
    a = abs((game["Prize"]["X"] * game["B"]["Y"] - game["Prize"]["Y"] * game["B"]["X"]) / 
            (game["A"]["X"] * game["B"]["Y"] - game["A"]["Y"] * game["B"]["X"]))
    b = abs((game["Prize"]["X"] * game["A"]["Y"] - game["Prize"]["Y"] * game["A"]["X"]) / 
            (game["A"]["X"] * game["B"]["Y"] - game["A"]["Y"] * game["B"]["X"]))
    
    # If it isn't an integer then we don't consider it possible to move to that location
    if (a.is_integer() and b.is_integer()):
        buttonPresses["A"] = int(a)
        buttonPresses["B"] = int(b)
    
    return buttonPresses

def process_games(data):
    totalPlays = []
    for game in data:        
        result = calculate_game_button_presses(game)
        totalPlays.append(result)

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