
with open("C:\Users\slick\source\repos\advent2024\day01\sample.txt", "r", encoding="utf8") as file:
    left = []
    right = []
    for line in file:
        values = [int(x) for x in line.split()]
        left.append(values[0])
        right.append(values[1])

    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        total += diff
    print(total)