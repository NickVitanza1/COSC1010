#
# Nicholas Vitanza
# 2/13/25
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
total = 0
bugs = 0

# Get number of bugs collected each day using a for loop.
for day in range(1, 8):
    print('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs

# Display the total number of bugs collected.
print('You collected a total of', total, 'bugs.')