# Coin Sentence Interpreter
# This script takes a sentence like "2 nickels and 3 dimes" and converts it to dollars

#set up coin values
coin_values = {
    "penny": 0.01,
    "pennies": 0.01,
    "nickel": 0.05,
    "nickels": 0.05,
    "dime": 0.10,
    "dimes": 0.10,
    "quarter": 0.25,
    "quarters": 0.25
}

#ask user for sentence
sentence = input("Enter a sentence with coin amounts (example: 2 nickels and 3 dimes): ")

#split the sentence
words = sentence.split()

# Start total at 0
total = 0.0

#go through the words
for i in range(len(words)):

    #if word is number
    if words[i].isdigit():
        amount = int(words[i])

        #look for the word coin

        if i + 1 < len(words):
            coin = words[i + 1].lower()
            # If the coin is in our dictionary
            if coin in coin_values:
                # Add to total
                total += amount * coin_values[coin]

#final dollar amount. rounded two decimals
print(f"{total:.2f}")