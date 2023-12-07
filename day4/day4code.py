import readInput

input = readInput.read_input("input.txt")

# input = [
# "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
# ]

copied_cards = []

points = 0

def evaluate_card(card):
    global points
    card_points = 0
    matching_numbers = 0
    card_data = card[card.index(":") + 2:].split()
    winners = card_data[:card_data.index("|")]
    numbers = card_data[card_data.index("|")+1:]
    
    for num in winners:
        if num in numbers:
            matching_numbers += 1
            if card_points == 0:
                card_points = 1
            else:
                card_points *= 2
    points += card_points
    
    for i in range(matching_numbers):
        copied_cards.append(input[card_index + i + 1])

for card_index, card in enumerate(input):
    evaluate_card(card)
    if card in copied_cards:
        for rcount in range(copied_cards.count(card)):
            evaluate_card(card)
        
print(len(copied_cards) + len(input))
print(points) # remove 2nd loop inside of line 39 to get part 1 solution