# Get info on a file

# Declare a variable with filename
filename = f"python_examples/text_files/file2.txt"

# Open file for reading
with open(filename, 'r') as f:
    text = f.read()

print(f"The content of the file {filename} is this:\n {text}") # Test the output
letters = sum(map(str.isalpha, text)) # Apply map function to every character in the string. If the character if alphanumeric, returns True, otherwise returns False, then sums the number of letters in that file with sum function
words = len(text.split()) # Splits words in a file into spaces and counts the number of words in that file`
lines = text.count('\n') + (not text.endswith('\n')) if text else 0 # text.count() - counts newline characters, not text.endswith - if the last line is missing a new line. Using ternary operator here

# Print the results
print(f"The number of letters in the {filename} file is {letters}")
print(f"The number of words in the {filename} file is {words}")
print(f"The number of lines in the {filename} file is {lines}")



