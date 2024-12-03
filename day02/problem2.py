import copy 

def is_safe(values):
    reverse = values[0] > values[len(values) - 1]
    copied_values = copy.deepcopy(values)
    copied_values.sort(reverse=reverse)
    if (values == copied_values):
        safe = True
        for i in range(len(values) - 1):
            diff = abs(values[i] - values[i + 1])
            if 0 == diff or diff  > 3:
                safe = False
                break
        return safe
    return False

with open("data.txt", "r", encoding="utf8") as file:
    safe_count = 0
    for line in file:
        values = [int(x) for x in line.split()]
        reverse = values[0] > values[len(values) - 1]

        if is_safe(values):
            safe_count += 1
        

    print(safe_count)
   