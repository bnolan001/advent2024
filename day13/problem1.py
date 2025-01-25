
with open("day13/sample.txt", "r", encoding="utf8") as file:
    data = []
    total = 0
    for line in file:
        data = [int(x) for x in line.strip().split()]

    

    print(total)