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
    usafe_data = []
    for line in file:
        values = [int(x) for x in line.split()]
        reverse = values[0] > values[len(values) - 1]

        if is_safe(values):
            safe_count += 1
        else:
            usafe_data.append(values)
    
    for data in usafe_data:
        for i in range(len(data)):
            sub_data = copy.deepcopy(data)
            del sub_data[i]
            if is_safe(sub_data):
                safe_count += 1
                break

    print(safe_count)
   