
def find_xmas_count(puzzle, x, y):
    count = 0
    possible_matches = []
    # left
    value = puzzle[y][x-3:x + 1]
    value = value[::-1]
    possible_matches.append(value)
        
    # right
    value = puzzle[y][x:x + 4]
    possible_matches.append(value)

    # up
    value = ""
    for i in range(4):
        value += puzzle[y-i][x]
    possible_matches.append(value)

    # down
    value = ""
    for i in range(4):
        value += puzzle[y+i][x]
    possible_matches.append(value)

    # diagonal up right
    value = ""
    for i in range(4):
        value += puzzle[y-i][x-i]
    possible_matches.append(value)

    # diagonal down right
    value = ""
    for i in range(4):
        value += puzzle[y+i][x+i]
    possible_matches.append(value)

    # diagonal up left
    value = ""
    for i in range(4):
        value += puzzle[y+i][x-i]
    possible_matches.append(value)

    # diagonal down left
    value = ""
    for i in range(4):
        value += puzzle[y-i][x+i]
    possible_matches.append(value)

    return possible_matches.count("XMAS")

with open("data.txt", "r", encoding="utf8") as file:
    puzzle = []
    for line in file:
        puzzle.append("****" + line.strip() + "****")
    
    mock_line = "*" * (len(puzzle[0]) - 1)
    puzzle.insert(0, mock_line )
    puzzle.insert(0, mock_line)
    puzzle.insert(0, mock_line)
    puzzle.insert(0, mock_line)
    puzzle.append(mock_line)
    puzzle.append(mock_line)
    puzzle.append(mock_line)
    puzzle.append(mock_line)
    total = 0
    
    for y in range(3, len(puzzle) - 2):
        row_total = 0
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == "X":
                found = find_xmas_count(puzzle, x, y)
                row_total += found
                total += found
        
    print(total)
   