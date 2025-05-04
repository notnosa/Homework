# script takes a sentence like "2 nickels and 3 dimes" and converts it to dollars

#coin values, including common typos
coin_v = {
    "penny": 0.01,
    "pennies": 0.01,
    "peny": 0.01,
    "penies": 0.01,

    "nickel": 0.05,
    "nickels": 0.05,
    "nickles": 0.05,
    "nickls": 0.05,

    "dime": 0.10,
    "dimes": 0.10,
    "dim": 0.10,
    "diems": 0.10,

    "quarter": 0.25,
    "quarters": 0.25,
    "quater": 0.25,
    "quaters": 0.25
}

# ask user for sentence
sentence = input("Enter a sentence with coin amounts (example: 2 nickels and 3 dimes): ")


words = sentence.split()


total = 0.0

# loop through all words
for i in range(len(words)):

    # if current word is a number
    if words[i].isdigit():
        amount = int(words[i])

        # try to get the coin type next
        if i + 1 < len(words):
            coin_word = words[i + 1].lower()

            # check if that word is in our coin list
            if coin_word in coin_v:
                total += amount * coin_v[coin_word]

# print total in dollars, 2 decimal places
print(f"{total:.2f}")