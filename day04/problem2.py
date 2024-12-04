import re

with open("data.txt", "r", encoding="utf8") as file:
    total = 0
    doing = True
    for line in file:
        cleaned_line = line
        
        if not doing and "do()" in cleaned_line:
            doing = True
            cleaned_line = cleaned_line[cleaned_line.index("do()") + 4:]

        while "don't()" in cleaned_line:
            dont_index = cleaned_line.index("don't()")
            if "do()" in cleaned_line[dont_index:]:
                do_index = cleaned_line.index("do()", dont_index)
                cleaned_line = cleaned_line[:dont_index] + cleaned_line[do_index + 4:]
            else:
                cleaned_line = cleaned_line[:dont_index]
                doing = False

        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", cleaned_line)
        for match in matches:
            numbers = match[4:len(match) - 1].split(",")
            total += int(numbers[0]) * int(numbers[1])

    print(total)
