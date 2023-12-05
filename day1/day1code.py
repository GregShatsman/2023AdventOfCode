import readInput

input = readInput.read_input("day1/input.txt")

# input = ['two1nine',        # test input
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen']

total = 0

numberdict = {
    "one": "1",
    "two": "2", 
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

for text in input:
    number = ""
    first_letter = ""
    last_letter = ""
    
    for index, letter in enumerate(text):
        if letter.isdigit():
            if first_letter == "":
                first_letter = letter
            last_letter = letter
            
        for i in range(6):                          # part 2
            if text[index:index+i] in numberdict:
                if first_letter == "":
                    first_letter = numberdict[text[index:index+i]] 
                last_letter = numberdict[text[index:index+i]]
                    
    print(first_letter)
    print(last_letter + "last")

    number = first_letter + last_letter
    
    total += int(number)
    
    print("total " + str(total))

print(total)
    
    