#
# Nicholas Vitanza
# 4/22/25
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Encryption Script - encrypt_script.py
def encrypt_file(input_file, output_file):
    # Define the dictionary that maps each letter to a symbol or number
    codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '*',
        'D': '$', 'd': '&', 'E': '(', 'e': ')', 'F': '^', 'f': '+',
        'G': '=', 'g': '-', 'H': '{', 'h': '}', 'I': '[', 'i': ']',
        'J': '|', 'j': ':', 'K': ';', 'k': ',', 'L': '.', 'l': '/',
        'M': '<', 'm': '>', 'N': '?', 'n': '~', 'O': '1', 'o': '2',
        'P': '3', 'p': '4', 'Q': '5', 'q': '6', 'R': '7', 'r': '8',
        'S': '0', 's': '-', 'T': '+', 't': '=', 'U': '#', 'u': '%',
        'V': '@', 'v': '&', 'W': '!', 'w': '*', 'X': '$', 'x': '^',
        'Y': '(', 'y': ')', 'Z': '[', 'z': ']'
    }

    try:
        # Open the input file (text.txt) and read its contents
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Encrypt the content by replacing each character using the dictionary
        encrypted = ''.join([codes.get(char, char) for char in content])
        # Note: characters not in the dictionary (like punctuation or numbers) are kept as-is

        # Write the encrypted content to the output file (encrypted.txt)
        with open(output_file, 'w') as outfile:
            outfile.write(encrypted)

        print(f"Encrypted and saved to '{output_file}'.")

    except FileNotFoundError:
        # This runs if the input file doesn't exist
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        # Catches any other errors that might occur
        print(f"Unexpected error: {e}")

# Run the function
encrypt_file('text.txt', 'encrypted.txt')