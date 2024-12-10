import pprint

map = []
with open("day06/sample.txt", "r", encoding="utf8") as file:
    total = 0
    
    for line in file:
        map += line.strip()

print('\n'.join([' '.join([str(cell) for cell in row]) for row in map]))
print(total)
   