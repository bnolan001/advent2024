with open("sample.txt", "r") as f:
    left = []
    right = []
    data = f.read().splitlines()
    for line in data:
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