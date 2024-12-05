

with open("data.txt", "r", encoding="utf8") as file:
    total = 0
    rules = {}
    correct_orderings = []
    for line in file:
        update_manual = []
        if "|" in line:
            first_page, second_page = line.strip().split("|")
            if first_page not in rules:
                rules[first_page] = []
            rules[first_page].append(second_page)

        elif "," in line:
            pages = line.strip().split(",")
            
            for page in pages:
                if page not in rules:
                    update_manual.append(page)
                else:
                    insert_index = len(update_manual)
                    for i in range(len(rules[page])):
                        if rules[page][i] in update_manual:
                            before_index = update_manual.index(rules[page][i])
                            if (before_index < insert_index):
                                insert_index = before_index
                            
                    update_manual.insert(insert_index, page)
            if update_manual == pages:
                correct_orderings.append(update_manual)
            print(update_manual)
    for pages in correct_orderings:
        index = len(pages) // 2
        total += int(pages[index])
    print(total)
   