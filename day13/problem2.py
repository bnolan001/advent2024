from datetime import datetime

def blink(stones):
    new_stones = {}
    for key, value in stones.items():
        if key == 0:
            if 1 in new_stones:
                new_stones[1] += value
            else:
                new_stones[1] = value
        elif len(str(key)) % 2 == 0:
            str_stone = str(key)
            stone = int(str_stone[0:len(str_stone) // 2])
            if stone in new_stones:
                new_stones[stone] += value
            else:
                new_stones[stone] = value
            stone = int(str_stone[len(str_stone) // 2:])
            if stone in new_stones:
                new_stones[stone] += value
            else:
                new_stones[stone] = value
        else:
            stone = key * 2024
            if stone in new_stones:
                new_stones[stone] += value
            else:
                new_stones[stone] = value
    
    return new_stones

with open("day11/data.txt", "r", encoding="utf8") as file:
    data = []
    total = 0
    for line in file:
        data = [int(x) for x in line.strip().split()]

    new_stones = {}
    for value in data:
        new_stones[value] = 1

    for i in range(75):
        new_stones = blink(new_stones)
            
    for key, value in new_stones.items():
        total += value

    print(total)