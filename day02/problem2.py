
with open("data.txt", "r", encoding="utf8") as file:
    left = []
    right = {}
    for line in file:
        values = [int(x) for x in line.split()]
        left.append(values[0])
        if values[1] not in right:
            right[values[1]] = 0
        right[values[1]] += 1

    left.sort()
    total = 0
    for i in range(len(left)):
        instances = 0 if left[i] not in right else right[left[i]] * left[i]
        total += instances
    print(total)