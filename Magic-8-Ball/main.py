#
# Nicholas Vitanza
# 4/3/25
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

# Function to read responses from the text file and return a list
def read_responses(filename):
    with open(filename, 'r') as file:
        responses = file.readlines()
    # Strip newline characters and return a list of responses
    return [response.strip() for response in responses]

# Function to simulate the Magic 8 Ball
def magic_8_ball():
    responses = read_responses("8_ball_responses.txt")  # Read responses from the file
    while True:
        question = input("Ask a yes or no question (or type 'quit' to stop): ")
        if question.lower() == 'quit':
            print("Thanks for playing! Goodbye.")
            break
        else:
            # Randomly select a response from the list
            response = random.choice(responses)
            print(f"Magic 8 Ball says: {response}")

# Run the Magic 8 Ball program
magic_8_ball()