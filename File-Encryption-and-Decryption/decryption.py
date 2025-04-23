def decrypt_file(input_file):
    # Define the reverse dictionary that maps symbols/numbers back to letters
    reverse_codes = {
        '%': 'A', '9': 'a', '@': 'B', '#': 'b', '!': 'C', '*': 'c',
        '$': 'D', '&': 'd', '(': 'E', ')': 'e', '^': 'F', '+': 'f',
        '=': 'G', '-': 'g', '{': 'H', '}': 'h', '[': 'I', ']': 'i',
        '|': 'J', ':': 'j', ';': 'K', ',': 'k', '.': 'L', '/': 'l',
        '<': 'M', '>': 'm', '?': 'N', '~': 'n', '1': 'O', '2': 'o',
        '3': 'P', '4': 'p', '5': 'Q', '6': 'q', '7': 'R', '8': 'r',
        '0': 'S', '+': 'T', '=': 't', '#': 'U', '%': 'u', '&': 'v',
        '*': 'w', '$': 'X', '^': 'x', '(': 'Y', ')': 'y', '[': 'Z',
        ']': 'z'
    }

    try:
        # Open the encrypted file and read its contents
        with open(input_file, 'r') as infile:
            encrypted_content = infile.read()

        # Decrypt the content by replacing each symbol using the reverse dictionary
        decrypted = ''.join([reverse_codes.get(char, char) for char in encrypted_content])
        # Again, non-dictionary characters are left unchanged

        # Display the decrypted content
        print("Decrypted content:")
        print(decrypted)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
decrypt_file('encrypted.txt')