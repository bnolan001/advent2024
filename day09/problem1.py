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
    new_disk = []
    end_index = len(disk) - 1
    for i in range(0, len(disk)):
        if i > end_index:
            break

        if disk[i] != ".":
            new_disk += [disk[i]]
            continue

        for j in range(end_index, i, -1):
            if disk[j] != ".":
                new_disk += [disk[j]]
                end_index = j - 1
                break

    return new_disk

def calculate_checksum(disk):
    checksum = 0
    for i in range(0, len(disk)):
        if disk[i] != ".":
            checksum += i * int(disk[i])
        else:
            print(f"Disk corrupted at index {i}")
    
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

