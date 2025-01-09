import re

def words_to_numbers(s):
    words_to_values = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
        "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000, "million": 1_000_000
    }
    
    tokens = s.lower().split()
    total = 0
    current = 0

    for word in tokens:
        if word in words_to_values:
            value = words_to_values[word]
            if value == 100:  # Multiply by 100
                current *= value
            elif value >= 1000:  # Multiply current by large numbers
                current *= value
                total += current
                current = 0
            else:
                current += value
    return total + current

# Input string
input_string = "three hundred million"

# Convert to number
output_number = words_to_numbers(input_string)

print(output_number)  # Output: 300000000
