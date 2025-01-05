import math

data = []

def build_disk(data):
    disk = []
    for i in range(0, int(math.ceil(len(data) / 2))):
        index = i * 2
        file_id = [i] * int(data[index])
        disk += file_id
        if (index + 1) < len(data):
            space = ["."] * int(data[index + 1])
            disk += space

    return disk

def compact_disk(disk):
    new_disk = disk
    copy_from_end_index = len(disk) - 1
    while copy_from_end_index  > 0:
        if new_disk[copy_from_end_index] == ".":
            copy_from_end_index -= 1
            continue
        copy_from_start_index = copy_from_end_index   
        for j in range(copy_from_end_index, 0, -1):
            if new_disk[j] != new_disk[copy_from_end_index]:
                copy_from_start_index = j + 1
                break

        data_size = copy_from_end_index - copy_from_start_index + 1
        available_size = 0
        copy_to_start_index = 0
        for j in range(0, copy_from_start_index):
            if new_disk[j] == ".":
                available_size += 1
                if available_size == 1:
                    copy_to_start_index = j
            else:
                available_size = 0

            if available_size >= data_size:
                break
        
        if available_size >= data_size:
            for j in range(copy_to_start_index, copy_to_start_index + data_size):
                new_disk[j] = disk[copy_from_start_index]
                new_disk[copy_from_start_index] = "."
                copy_from_start_index += 1

        copy_from_end_index = copy_from_end_index - data_size        

    return new_disk

def calculate_checksum(disk):
    checksum = 0
    for i in range(0, len(disk)):
        if disk[i] != ".":
            checksum += i * int(disk[i])
    
    return checksum

with open("day09/data.txt", "r", encoding="utf8") as file:
    total = 0
    for line in file:
        if line.strip() == "":
            continue
        data = list(line.strip())
    raw_disk = build_disk(data)
    compacted_disk = compact_disk(raw_disk)
    total = calculate_checksum(compacted_disk)
    print(total) 

