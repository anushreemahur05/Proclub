import json
from difflib import get_close_matches
data= json.load(open("original.json"))

def FindInDictionary(word):
    word=word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title]

    elif word.upper() in data:
        return data[word.upper]

    elif len(get_close_matches(word,data.keys())) > 0 :

        print("Did you mean %s instead " %get_close_matches(word , data.keys())[0])
        decide = input("Press y for Yes and n for No\n")

        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            return("WORD NOT FOUND")
        else:
            return("You have entered the wrong input")
    else:
        return("WORD NOT FOUND")


print("DICTIONARY:")
w= "y"

while w=="y":
     word=input("Enter the word you want to search:\n")
     ans=FindInDictionary(word)
     if type(ans)== list:
         for item in ans:
             print(item)
     else:
        print(ans)

     w=input("Enter y if you want to search another word: ")

print("END")
