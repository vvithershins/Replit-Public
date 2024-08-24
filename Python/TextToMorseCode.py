# Define the Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'  # Space between words
}

def text_to_morse(text):
    # Convert text to upper case for consistency
    text = text.upper()

    # Convert each character to Morse code
    morse_code = [MORSE_CODE_DICT[char] for char in text if char in MORSE_CODE_DICT]

    # Join the Morse code with a space
    return ' '.join(morse_code)

# Take input from the user
input_text = input("Enter a string to convert to Morse code: ")

# Convert the input text to Morse code
morse_output = text_to_morse(input_text)

# Output the Morse code
print("Morse Code:", morse_output)
