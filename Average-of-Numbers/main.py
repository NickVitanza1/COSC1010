#
# Nicholas Vitanza
# 3/14/25
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Open the file for reading
try:
    with open('numbers.txt', 'r') as file:
        # Read the contents of the file and split them into a list of strings
        numbers = file.read().split()
        
        # Convert the list of strings to integers
        numbers = [int(num) for num in numbers]
        
        # Calculate the average
        if len(numbers) > 0:
            average = sum(numbers) / len(numbers)
            print(f"The average is: {average}")
        else:
            print("The file is empty.")
except FileNotFoundError:
    print("The file 'numbers.txt' was not found.")
except ValueError:
    print("The file contains non-integer values.")