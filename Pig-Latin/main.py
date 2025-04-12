#
# Nicholas Vitanza
# 4/11/25
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def convert_to_pig_latin(word):
    # Move the first letter to the end and add "ay"
    if len(word) > 1:
        return word[1:] + word[0] + "ay"
    else:
        return word + "ay"

def pig_latin_sentence(sentence):
    words = sentence.split()
    pig_latin_words = [convert_to_pig_latin(word) for word in words]
    return ' '.join(pig_latin_words)

# Get input from the user
user_input = input("Enter a sentence: ")
converted = pig_latin_sentence(user_input)
print("Pig Latin:", converted)