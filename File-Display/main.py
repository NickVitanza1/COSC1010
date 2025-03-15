#
# Nicholas Vitanza
# 3/14/25
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Open the file
myfile = open('numbers.txt', 'r')

# Read and diplay the files contents
for line in myfile:
    number = int(line)
    print(number)

# Close the file
myfile.close()