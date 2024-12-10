
map = []
with open("day06/sample.txt", "r", encoding="utf8") as file:
    total = 0
    
    for line in file:
        map += line.strip()

    print(map)
    print(total)
   