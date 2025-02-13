#
# Nicholas Vitanza
# 2/8/25
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
length1 = 0
width1 = 0
length2 = 0
width2 = 0
area1 = 0
area2 = 0

# Get length 1
length1 = int(input('Enter the length of rectangle 1: '))

# Get width 1
width1 = int(input('Enter the width of rectngle 1: '))

# Get length 2
length2 = int(input('Enter the length of rectangle 2: '))

# Get width 2
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate area 1
area1 = length1 * width1

# Calculate area 2
area2 = length2 * width2

# Print area comparison using if-elif-else statements
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area')