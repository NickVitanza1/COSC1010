#
# Nicholas Vitanza
# 4/14/25
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

def create_state_capital_dict():
    """Creates a dictionary of U.S. states and their capitals."""
    return {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'Saint Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
    }

def quiz_user(state_capitals):
    """Quizzes the user on state capitals and tracks correct/incorrect responses."""
    correct = 0
    incorrect = 0
    states = list(state_capitals.keys())
    random.shuffle(states)

    for state in states:
        capital = state_capitals[state]
        answer = input(f"What is the capital of {state}? ").strip().lower()
        if answer == capital.lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The capital of {state} is {capital}.")
            incorrect += 1

    print(f"\nYou got {correct} correct and {incorrect} incorrect.")

def main():
    """Main function to run the quiz."""
    state_capitals = create_state_capital_dict()
    quiz_user(state_capitals)

if __name__ == "__main__":
    main()
