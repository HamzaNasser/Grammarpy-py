# Step 1: Install the PyEnchant library
# pip install pyenchant

# Step 2: Import the library and create an instance of the DictWithPWL class
import enchant
import re

def process_text(text: str) -> str:
    # Split the text into a list of words
    words = text.split()

    # Capitalize the first word
    words[0] = words[0].capitalize()

    # Check if the text is a question
    is_question = words[-1].endswith("?")

    # Add a comma before the FANBOY conjunctions
    for i in range(1, len(words) - 1):
        if words[i].lower() in ["but", "for", "so", "and", "or", "yet"]:
            words[i - 1] += ","
        # Capitalize the letter "i" if it appears at the beginning of a word
        elif len(words[i]) == 1 and words[i] == "i":
            words[i] = "I" + words[i][1:]

    # Join the list of words into a single string and add a period or question mark at the end
    processed_text = " ".join(words) + "." if not is_question else " ".join(words) + "?"

    return processed_text

def add_question_mark(sentence: str) -> str:
    # Split the sentence into a list of words
    words = sentence.split()
    
    # Set a flag to track whether all question words have been found
    all_question_words_found = True
    
    # Check if all of the question words are present in the list
    for question_word in ["where", "what", "why"]:
        if question_word not in words:
            all_question_words_found = False
            break
    
    # If all question words were found, add a question mark to the end of the sentence and return it
    if all_question_words_found:
        return sentence + "?"
    
    # If not all question words were found, return the original sentence
    return sentence



dictionary = enchant.DictWithPWL("en_US", "personal_words.txt")

print("\033[92m" + r"""
  _____  _       _           _ 
 |_   _|| |     | |         | |
   | |  | |_ __ | |__   ___ | |
   | |  | | '_ \| '_ \ / _ \| |
  _| |_ | | | | | | | | (_) | |
 |_____||_|_| |_|_| |_|\___/|_|
                                 
""" + "\033[0m")
print("\033[92m" + "Grammarpy" + "\033[0m")
print("\033[93mBy Hamza\033[0m")

# Step 3: Use the check method to find misspelled words in a piece of text
text = input("Enter a sentence: ")
words = text.split()

# Step 4: Use the suggest method to get a list of suggested corrections for a misspelled word
corrected_words = []
for word in words:
    if dictionary.check(word):
        corrected_words.append(word)
    else:
        suggestions = dictionary.suggest(word)
        if suggestions:
            print(f"\033[91mIncorrect spelling: {word}\033[0m")
            print(f"\033[92mSuggestions: {suggestions}\033[0m")
            choice = input("Enter the number of the suggestion you want to use (or press Enter to keep the original word): ")
            if choice == "":
                corrected_words.append(word)
            else:
                corrected_words.append(suggestions[int(choice) - 1])
        else:
            corrected_words.append(word)

# Step 5: Join the corrected words to form the corrected text
corrected_text = " ".join(corrected_words)
corrected_text =  add_question_mark(corrected_text)

print(f"\033[94mCorrected text: {process_text(corrected_text)}\033[0m")
