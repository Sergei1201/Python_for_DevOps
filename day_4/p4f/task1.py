# Task 1. Find files that contain text the user is searching for

# Import the os module
import os

# Initialize the folder variable that contains our files
folder = r"python_examples/text_files"

# Initialize a variable for searching a substring from the user input
search = input()

# Initialize a variable to store file names that contain the information the user is searching for
answ = set()

# Display all the files that are within our
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    print(filepath)

# Search for info in the files. If there's a match, add the name of that file into the set (unique names)
for filename in os.listdir(folder):
    filepath_with_file_name = os.path.join(folder, filename)
    print(filepath_with_file_name)

    # Open file in the read only mode
    with open(filepath_with_file_name, 'r') as fp:
        for line in fp:
             if search in line:
                answ.add(filename)
    
# Print the filenames that satisfy the search criteria onto the screen by looping through the set
print(answ)

