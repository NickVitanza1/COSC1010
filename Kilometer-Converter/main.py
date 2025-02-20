#
# Nicholas Vitanza
# 2/20/25
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Variables
kilometers = 0
miles = 0
CONVERSION_FACTOR = 0.6214

def main():

    # Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles
    show_miles(kilometers)

def show_miles(km):

    # Calculate miles
    miles = km * CONVERSION_FACTOR

    # Display the miles
    print(km, 'kilometers equals', miles, 'miles.')

# Call the main function
main()