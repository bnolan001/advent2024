import re

with open("data.txt", "r", encoding="utf8") as file:
    total = 0
    for line in file:
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for match in matches:
            numbers = match[4:len(match) - 1].split(",")
            total += int(numbers[0]) * int(numbers[1])

    print(total)
   