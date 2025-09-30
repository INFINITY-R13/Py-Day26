# main.py

import pandas

# Read the CSV file containing the NATO phonetic alphabet into a pandas DataFrame.
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame using a dictionary comprehension.
# This format is more efficient for lookups than searching the DataFrame every time.
# {new_key:new_value for (index, row) in df.iterrows()}
# Example: {"A": "Alfa", "B": "Bravo", ...}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic_code():
    """Gets user input and prints the corresponding NATO phonetic code list."""
    # Prompt the user for a word and convert it to uppercase for matching.
    word = input("Enter a word: ").upper()

    try:
        # Use a list comprehension to find the phonetic code for each letter.
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        # Handle the error if the user enters a number or symbol not in the dictionary.
        print("Sorry, only letters in the alphabet please.")
        # Call the function again to give the user another chance.
        generate_phonetic_code()
    else:
        # This block runs only if the 'try' block completes without errors.
        print(output_list)

# Start the program by calling the function.
generate_phonetic_code()