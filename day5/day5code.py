import readInput

input = readInput.read_input("input.txt")


known = {
    "seed": [],
    "soil": [],
    "fertilizer": [],
    "water": [],
    "light": [],
    "temperature": [],
    "humidity": [],
    "location": []
}

map_lists = " ".join(input).split('  ')

for seed in map_lists[0].split():
    if seed.isdigit():
        known["seed"].append(seed)

map_lists = map_lists[1:]

for map in map_lists:
    cut_map = map.split(': ')
    map_from = cut_map[0][:cut_map[0].index('-to')]
    map_to = cut_map[0][cut_map[0].index('to-')+3:cut_map[0].index(' map')]
    submaps = []
    
    for i, num in enumerate(cut_map[1].split()):
        if i % 3 == 0:
            submaps.append([])
            submaps[int(i/3)].append(cut_map[1].split()[i])
            submaps[int(i/3)].append(cut_map[1].split()[i+1])
            submaps[int(i/3)].append(cut_map[1].split()[i+2])

    for num in known[map_from]:
        for i, submap in enumerate(submaps):
            if int(num) >= int(submap[1]) and int(num) < int(submap[1]) + int(submap[2]):
                num_to_add = int(submap[0]) - int(submap[1]) + int(num)
                known[map_to].append(num_to_add)
                break
            elif i == len(submaps) - 1:
                known[map_to].append(num)
                continue

curr_num = 9999999999999999999999999

for num in known["location"]:
    if num < curr_num:
        curr_num = num

print(curr_num)