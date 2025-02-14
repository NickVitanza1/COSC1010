#
# Nicholas Vitanza
# 2/13/25
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Variables
budget = 0
expenses = 0
total = 0

# Get the budget of a user
budget = int(input('Enter the budget of the month: '))
another = 'y'  # Variable to control the loop

# Declare the accumulator
total = 0.0

# Process one or more expenses
while another == 'y' or another == 'Y':
    # Get the expenses
    expenses = float(input('Enter the expenses: '))
    total += expenses
    # Do this again ?
    another = input('Do you have another expenses? ' +
                    '(Enter y for yes): ')

if total > budget:
    print(f'You are ${total - budget} over the budget ')
elif total == budget:
    print(f'Your budget is enough for expenses!')
else:
    print(f'You are ${total - budget} under the budget ')

print(f'Total: ${total}')
