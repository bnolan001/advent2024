import copy 

with open("sample.txt", "r", encoding="utf8") as file:
    safe_count = 0
    for line in file:
        values = [int(x) for x in line.split()]
        reverse = values[0] > values[len(values) - 1]

        copied_values = copy.deepcopy(values)
        copied_values.sort(reverse=reverse)
        print(values, "|", copied_values)
        if (values == copied_values):
            for i in range(len(values) - 1):
                if 1 >= abs(values[i] - values[i + 1]) <= 3:
                    safe_count += 1
                    break

    print(safe_count)
   