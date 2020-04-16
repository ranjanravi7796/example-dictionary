import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def example(key):
    key = str.casefold(key)
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()] 
    elif len(get_close_matches(key,data.keys())) > 0:
        yn = input('Did you mean %s instead?  Reply Y if yes, or N if no: ' % get_close_matches(key,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(key,data.keys())[0]]
        elif yn == 'N':
            return 'The word is not available for No'
        else:
            return 'cant understand press Y or N only'
    else:
        return 'The word is not available'

key = input('enter a word: ')
output = example(key)

if type(output) == list:
    for item in output:
        print(': '+item)
else:
    print(output)

