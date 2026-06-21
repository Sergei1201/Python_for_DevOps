# Lists, tuples and dictionary tasks

# Working with lists in Python
# Task 1. Generate a list of in integers

# import the random module to generate let's say 10 numbers in a range from 1 to 100
import random

# Using list comprehension
list1 = [random.randint(1, 100) for _ in range(10)]
# print(list1) - test the output

# Task 2. Explore the dir command
print(dir(list1))# Returns a list of possible methods with lists

# Task 3. Using some methods to work with lists
list1.append(1) # Appends to the end of the list, modifies the original list
print(list1)
list1.sort() # Sort the list from min to max, modifies the original list
print(list1)
list1.remove(1) # Remove an element from the list, modifies the list
print(list1)
list1.reverse() # Reverse the list, modifies the original list
print(list1)
list1.insert(0, 150) # Insert an element into the list to a specific position
print(list1)

# Task 4. Change some elements of the list using indexing
list1[2] = 501
list1[9] = 1000
print(list1)

# Task 5. Append a new element to the end of the list
list1.append(2000)
print(list1)

# Task 6. Add a new element to the list to any position
list1.insert(10, 2500) # Adding 2500 to the 10-th position
print(list1)

# Task 7. Remove an element from the list from the certain position
list1.pop(2) # Removes the element from the position #2 and returns it
print(list1)
# Task 8. Remove the last element from the list
list1.pop() # Pops out the last element from the list
print(list1)

# SORTING LISTS

# Task 1. Sort list in the descent order
list1.sort(reverse=True)

# Task 2. Make sure the list is in the reverse order
print(list1)

# Using the sorted() function to not modified the original list
print(sorted(list1))
# Make sure the original list hasn't got modified
print(list1)

# Task 3. Create a new list of random elements (list2). Let's create 10 elements
list2 = [random.randint(1, 100) for _ in range(10)]
print(list2)

# Task 4. Create a new list based on the previous one (but sorted)
list3 = sorted(list2)
print(list3)

# Task 5. Check out the elements of the list2 and list 3
print(list2, list3)

# WORKING WITH TUPLES

# Task 1. Use the dir command on a tuple
print(dir(tuple)) # Returns a list of possible methods on a tuple

# Task 2. Call the help command to study the index() and count() methods
# print(help(tuple.count))
# print(help(tuple.index))

# Task 3. Create a tuple of some numbers
seq = (10, 22, 21, 19, 55, 77, 23)

# Task 4. Determine what the methods count() and index() return when applied to the tuple
print(seq.count(22)) # Returns the number of given elements in the tuple
print(seq.index(55)) # Returns the index of the given element

# Task 5. Convert the tuple to a list
listseq = list(seq) # Returns a list from the tuple
print(listseq)

# Task 6. Check if the conversion was correct
print(type(listseq)) # Returns list class

# Task 7. Check all general method for the converted tuple
listseq.reverse()
print(listseq)
listseq.append(5)
print(listseq)
listseq.remove(22)
print(listseq)
listseq.pop()
print(listseq)
listseq.pop(0)
print(listseq)
listseq.insert(1, 100)
print(listseq)
listseq.sort()
print(listseq)

# WORKING WITH DICTIONARIES

# Task 1. Create a dictionary
person = {
        "first_name" : "John",
        "last_name" : "Doe",
        "age" : 35,
        "occupation" : "Web developer"
        }

print(person)

# Task 2. Access values of the dictionary
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["occupation"])

# Tasks 3/4. Create an empty dictionary and fill it with values from the user input
student = {}
student["name"] = input("Enter a name for a dictionary ")
student["age"] = input("Enter an age for a dictionary ")
print(student)

# Handling complex data in a dictionary
# Task 1. Create a dictionary with complex data
person2 = {
        "name" : {"first_name": "John", "last_name" : "Doe"},
        "jobs" : ["Web Dev", "DevOps"],
        "age" : 39
        }
# Task 2. Print the first name and the list of the jobs
print(person2["name"]["first_name"])
print(person2["jobs"])

# Task 3. Extend information about the person created above
person2["jobs"].append("DevSecOps")

# Task 4. Print the full info on the person2
print(person2)






