import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no -> " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry, I don't understand your input."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter the word to search for: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
