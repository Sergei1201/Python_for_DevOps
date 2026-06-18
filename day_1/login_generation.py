# A program that generates a login from the first and last names of the user

# Suggest the user to enter their first and last names (as one string)
name = input("Enter your first and last names: ")

# Convert the name to the title case (the first letter of each word should be capitalized)
name_title = name.title()

# Split the full name (string) into a list (first and last names included) - returns a list ["first_name", "last_name"]
name_part = name_title.split()

# Getting the first and last name from the list
first_name = name_part[0]
last_name = name_part[1] 

# Generate a login from the 4 letters of the last name and the first letter of the first name
user_login = last_name[:4] + first_name[0]

# Show ouput to the user
print(f"=====A login for the user {first_name} {last_name} has been generated=====:\n {last_name} {first_name}: {user_login}")

# print(name_part, first_name, last_name, user_login) # Testing the ouput
