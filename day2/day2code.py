import readInput
import re

input = readInput.read_input("input.txt")

# input = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
# "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
# "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
# "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
# "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

output = 0
games = []
total_ids = 0
power = 0

limits = {"red": 0, "green": 0, "blue": 0} 

for game in input:
    games.append(re.split(': |, |; ', game))

for game in games:
    limits = {"red": 0, "green": 0, "blue": 0} 
    for i, check in enumerate(game):
        if i == 0:
            game_id = check[4:]
            total_ids += int(game_id)
        
        elements = check.split()
        # if elements[0] != 'Game' and int(elements[0]) > limits[elements[1]]: 
        #     output += int(game_id)    PART 1 --- RETURNS INVERSE OF ANSWER (total game_ids - answer)
        #     break
        
        if elements[0] != 'Game':
            if (int(elements[0]) > limits[elements[1]]):
                limits[elements[1]] = int(elements[0])
                
    output += limits["red"]*limits["green"]*limits["blue"]
        
        
print(output)