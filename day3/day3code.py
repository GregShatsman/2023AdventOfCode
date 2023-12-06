import readInput

input = readInput.read_input("input.txt")

# input = [
# '467..114..',
# '...*......',
# '..35..633.',
# '......#...',
# '617*......',
# '.....+.58.',
# '..592.....',
# '......755.',
# '...$.*....',
# '.664.598..']

sum = 0
part_two_sum = 0
nums = []
current_num = ""
next_door_col = 0
row_above = ''
row_below = ''
gear_ids = {}

def contains_part(string):
    for char in string:
        if char != '.' and not char.isdigit():
            return True

def contains_gear(string):
    for char in string:
        if char == '*':
            return True
    

for row_num, row in enumerate(input):
    current_num = ""
    for col, char in enumerate(row):
        if char == "*":
            gear_ids[str(row_num) + ' ' + str(col)] = []

for row_num, row in enumerate(input):
    current_num = ""
    for col, char in enumerate(row):
        if char.isdigit() and not col == len(row) -1:
            current_num += char
        elif col == len(row) -1  or not char.isdigit():
            if col == len(row) - 1 and char.isdigit():
                current_num += char
            next_door = ''
            char_after = row[col]
            
            # check if number is a part
            start_of_num = 0
            end_of_num = col + 1
            
            if col != end_of_num:
                end_of_num = col + 1
                
            if col - len(current_num) - 1 > 0:
                start_of_num = col - len(current_num) - 1
                    
            next_door = row[col-len(current_num)-1]
            next_door_col = col-len(current_num)-1
            
            if col == len(row) - 1 and char.isdigit():    # figure out all cases when number is on an edge
                char_after = ''
                next_door = row[col-len(current_num)]
                next_door_col = col-len(current_num)
                start_of_num += 1
            
            if col - len(current_num) == 0:
                next_door = ''
            
            if row_num != 0:
                row_above = input[row_num-1]
                
            if row_num != len(row)-1:
                row_below = input[row_num+1]
            else:
                row_below = ''
                
            surrounding = ''
            
            if current_num != '':
                surrounding += row_above[start_of_num:end_of_num] + next_door + char_after + row_below[start_of_num:end_of_num]
                
            if contains_part(surrounding):
                if current_num != '':
                    nums.append(current_num)
            
            # P2 -- Assumes part can only ever have 1 gear touching it
            if contains_gear(surrounding):
                gear_row = 0
                gear_col = 0
                
                if contains_gear(row_above[start_of_num:end_of_num]):
                    gear_row = row_num - 1
                    gear_col = col - len(row_above[start_of_num:end_of_num]) + row_above[start_of_num:end_of_num].index('*') + 1
                elif contains_gear(next_door):
                    gear_row = row_num
                    gear_col = next_door_col
                elif contains_gear(char_after):
                    gear_row = row_num
                    gear_col = col
                elif contains_gear(row_below[start_of_num:end_of_num]):
                    gear_row = row_num + 1
                    gear_col = col - len(row_below[start_of_num:end_of_num]) + row_below[start_of_num:end_of_num].index('*') + 1

                gear_ids[str(gear_row) + ' ' + str(gear_col)].append(int(current_num))
      
            current_num = ""
            surrounding = ''
                
for gear in gear_ids:
    if len(gear_ids[gear]) == 2:
        part_two_sum += gear_ids[gear][0] * gear_ids[gear][1]

for num in nums:
    if num != '':
        sum += int(num) 

print(sum)
print(part_two_sum)