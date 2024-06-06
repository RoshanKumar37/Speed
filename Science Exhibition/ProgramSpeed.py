import os
import csv
import re
import random
from SetupSpeed import speak


# ---------------------------------------------------------
os.system('jupyter nbconvert --to python SetupSpeed.ipynb')
# ---------------------------------------------------------

# Functions -------------------------------------------------------------------------------------------------------

def preprocess_input(user_input):

    replacements = {

        # Same Stuffs
        
        "what's": "what is",
        "whats": "what is",
        "how is": "how's",
        "I am": "I'm",
        "who's" : "who is",
        "one more joke": "tell me a joke"
    }

    for alt_phrase, canonical_form in replacements.items():
        user_input = re.sub(r'\b' + alt_phrase + r'\b', canonical_form, user_input, flags=re.IGNORECASE)
    
    return user_input


def load_database(file_path):
    database = {}
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter='-')
        for row in reader:
            user_text, response = row['userText'], row['response']
            database[user_text.lower()] = response
    return database


def get_random_jokes():
    random.choices('a', 'b', 'c')


def get_response(database, user_input):
    return database.get(user_input, "Sorry, I don't understand that.")


def main():
    database_file = 'Databases/database.csv'

    database = load_database(database_file)

    while True:

        user_input = input("You: ")

        if user_input.lower() == 'exit' or user_input.lower() == "bye!":
            print("Goodbye!")
            speak("Goodbye!")
            break

        user_input = preprocess_input(user_input)

        response = get_response(database, user_input)
        print("Bot:", response)
        speak(response)





if __name__ == "__main__":
    main()