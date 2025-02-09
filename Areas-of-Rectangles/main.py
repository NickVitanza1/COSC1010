#
# Nicholas Vitanza
# 2/8/25
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables

# Get length A
lengthA = int(input('Enter the length of rectangle 1: '))
# Get width A
widthA = int(input('Enter the width of rectngle 1: '))
# Get length B
lengthB = int(input('Enter the length of rectangle 2: '))
# Get width B
widthB = int(input('Enter the width of rectangle 2: '))
# Calculate area A
areaA = lengthA * widthA
# Calculate area B
areaB = lengthB * widthB
# Print area comparison using if-elif-else statements
if areaA > areaB:
    print('Rectangle A has the greater area.')
elif areaA > areaB:
    print('Rectangle B has the greater area.')
else:
    print('Both have the same area')