#
# Nicholas Vitanza
# 3/27/25
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        numbers = []
        for line in lines:
            try:
                # Attempt to convert each line to a number
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Warning: '{line.strip()}' is not a valid number and will be skipped.")

        if len(numbers) == 0:
            print("No valid numbers to calculate an average.")
            return None
        
        average = sum(numbers) / len(numbers)
        return average

    except IOError:
        print(f"Error: Could not read the file '{filename}'. Please check if the file exists and is accessible.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
filename = 'numbers.txt'
average = calculate_average(filename)

if average is not None:
    print(f"The average of the numbers is: {average}")