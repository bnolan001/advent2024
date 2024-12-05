
def find_xmas_count(puzzle, x, y):
    count = 0
    possible_matches = []
    # left
    value = puzzle[y-1][x-1] + puzzle[y][x] + puzzle[y+1][x+1]
    if "MAS" in value or "SAM" in value:
        count += 1
    
    value = puzzle[y+1][x-1] + puzzle[y][x] + puzzle[y-11][x+1]
    if "MAS" in value or "SAM" in value:
        count += 1

    return count == 2

with open("sample.txt", "r", encoding="utf8") as file:
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
            if puzzle[y][x] == "A":
                found = find_xmas_count(puzzle, x, y)
                row_total += found
                total += found
        
    print(total)
   