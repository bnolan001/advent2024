import copy 

with open("sample.txt", "r", encoding="utf8") as file:
    safe_count = 0
    for line in file:
        values = [int(x) for x in line.split()]
        reverse = values[0] > values[len(values) - 1]

        copied_values = copy.deepcopy(values)
        copied_values.sort(reverse=reverse)
        if (values == copied_values):
            safe = True
            for i in range(len(values) - 1):
                if 0 == abs(values[i] - values[i + 1]) > 3:
                    safe = False
                    break
            if safe:
                print("Safe",values, "|", copied_values)
                safe_count += 1
            else:
                print("Unsafe",values, "|", copied_values)
        else:
            print("Unsafe",values, "|", copied_values)


    print(safe_count)
   