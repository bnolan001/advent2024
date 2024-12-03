import copy 

with open("sample.txt", "r", encoding="utf8") as file:
    safe_count = 0
    for line in file:
        values = [int(x) for x in line.split()]
        copied_values = copy.deepcopy(values).sort()
        if (values == copied_values):
            for i in range(len(values) - 1):
                if 1 >= abs(values[i] - values[i + 1]) <= 3:
                    safe_count += 1
    print(safe_count)
   