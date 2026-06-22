# A program that tests if a ticket is lucky
# The logic of the program: the ticket should contain 6 digits. If the sum of the first 3 digits is equal to the sum of the last 3 digits of the ticket, the ticket is considered to be lucky, otherwise it's not.

# Ask the user for the 6-digit input of the ticket
ticket_num: str = input("Enter a 6-digit ticket: ")

# Test the output
print(ticket_num)

# Input validation (check if the length of the num is 6 and it's a number
if (len(ticket_num) == 6 and ticket_num.isdigit()):

    # Split the number in 2 parts, then add nums and compare to compare 2 parts
    part_one_sum: int = sum(int(digit) for digit in ticket_num[:3])
    part_two_sum: int = sum(int(digit) for digit in ticket_num[3:])

    # Test the output
    print(part_one_sum)
    print(part_two_sum)

    # Compare the 2 number to determine if there's a match
    if (part_one_sum == part_two_sum):
       
       # The ticket is lucky
       print(f"The ticket {ticket_num} is lucky. You win!")
    
       # Otherwise, the ticket is unlucky and you lose
    else:
       print(f"The ticket {ticket_num} is not lucky. You lose!")

# Otherwise, tell the user that the input is invalid
else:
    print("The input is not valid. The number should contain 6-digits")


