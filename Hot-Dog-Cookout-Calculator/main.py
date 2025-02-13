#
# Nicholas Vitanza
# 2/8/25
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Constants
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Local variables
numAttending = 0    # The number of people attending
numPerPerson = 0    # The number of hot dogs and buns per person
total = 0           # The total number of hot dogs and buns needed
minDogs = 0         # The minimum number of packages of hot dogs
minBuns = 0         # The minimum number of packages of hot dog buns
dogsLeft = 0        # The number of hot dogs leftover from a package
bunsLeft = 0        # The number of hot dog buns leftover from a package

# Get the number of people attending the cookout from the user.
numAttending = int(input('Enter the number of people attending the cookout: '))

# Get the number of hot dogs per person from the user.
numPerPerson = int(input('Enter the number of hot dogs per person: '))

# Calculate the total number of hot dogs and buns needed.
total = numAttending * numPerPerson

# Calculate the minimum number of packages of hot dogs needed.
minDogs = total // HOT_DOGS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of hot dogs.
if minDogs > 0:
    # Calculate the number of hot dogs leftover from a package if any.
    dogsLeft = total % HOT_DOGS_PER_PACKAGE

    # If there will be leftovers, add an additional package of hot dogs
    if dogsLeft != 0:
        minDogs += 1

# Set the minimum number of packages of hot dogs to one beause the number of people attending is small enough to require only one package of hot dogs
else:
    minDogs = 1

# Determine the number of leftover hot dogs, if any.
dogsLeft = (HOT_DOGS_PER_PACKAGE * minDogs) - total

# Calculate the minimum number of packages of buns needed.
minBuns = total // BUNS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of buns.
if minBuns > 0:
    # Calculate the number of hot dogs leftover from a package if any.
    bunsLeft = total % BUNS_PER_PACKAGE
   
    # If there will be leftovers, add an additional package of hot dogs
    if bunsLeft != 0:
        minBuns += 1

# Set the minimum number of packages of hot dogs to one beause the number of people attending is small enough to require only one package of hot dogs
else:
    minBuns = 1

# Display the minimum packages of hot dogs needed.
print('Minimum packages of hot dogs needed: ', minDogs)

# Display the minimum packages of hot dog buns needed.
print('Minimum packages of hot dog buns needed: ', minBuns)

# Display the number of hot dog buns leftover.
print('Hot dogs leftover: ', dogsLeft)

# Display the number of hot dog buns leftover.
print('Hot dog buns leftover: ', bunsLeft)