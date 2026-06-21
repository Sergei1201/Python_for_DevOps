# Program that creates a word based on the first letters of words entered by the user

# Initialize an empty list to store words
word_list: list = []

# Ask the user for the input
print("Enter words (one by one)")
print("=" * 30) # Formatting the initial output

# Repeat input until the empty string is entered
while True:
    user_word: str = input("Type in a new word: ")

    # Checking if the input is empty (the user hits Enter)
    if user_word == "":
        break # Break out of the loop

    # Add words to our list
    word_list.append(user_word)

    # Test the output
    # print(word_list)

# Take out the first letter of every word in the word list to create a new phrase
new_phrase: str = "" # our new phrase string, for now it's empty

# Append letters of each word to the string (+= operator used) and convert it to the upper case so that the new phrase will be capitalized
for w in word_list:
    new_phrase += w[0].upper()

# Show output to the screen
print("The results")
print("=" * 30) # Formatting
print(f"The words that have been typed in by the user: {word_list}")
print(f"New phrase generated from the first letters of each word:", end=' ')
print(new_phrase)





