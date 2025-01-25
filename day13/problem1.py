def blink(stones):
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == 0:
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            str_stone = str(stones[i])
            new_stones.append(int(str_stone[0:len(str_stone) // 2]))
            new_stones.append(int(str_stone[len(str_stone) // 2:]))
        else:
            new_stones.append(stones[i] * 2024)
    
    return new_stones

with open("day11/data.txt", "r", encoding="utf8") as file:
    data = []
    total = 0
    for line in file:
        data = [int(x) for x in line.strip().split()]

    #print(data)
    new_stones = data
    for i in range(25):
        new_stones = blink(new_stones)
        #print(new_stones)
    
    print(len(new_stones))