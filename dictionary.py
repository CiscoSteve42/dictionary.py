import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no " % get_close_matches(word, data.keys())[0])
        if yn == "y".lower():
            return data[get_close_matches(word, data.keys())[0]]
        elif yn =="n".lower():
            return "Word is not available."
        else:
            return "Entry Not Understood."
    else:
        return "Word is not available."
word = input("Enter word: ")

print(translate(word))
