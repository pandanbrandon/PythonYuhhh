"""
    Program: idk yet    
    Name: Brandon Thammasine   
    Date: 1/5/25
"""

# word analyzer - give frequency of each word,
# in decending order, most frequent on top


text = "She's toxic for the thrill of it, bad news but im into it I chase that dragon all the time. She knows how to reel me in, use me up and she's gone again, oh my. I stick around for the high."

# method to clean string - remove commas and periods (,.)
def cleanText(text):
    charsToRemove = ",."

    translationTbl = str.maketrans("", "", charsToRemove)

    cleanedText = text.translate(translationTbl)

    return cleanedText

# call cleanText to clean text
readyText = cleanText(text)

# converts string to dict - all words are keys and set to 0
textWordCount = {word: 0 for word in readyText.split()}

print(textWordCount)


# -----------------

# Dictionary

person = {
    "name": "Brandon",
    "age": 24,
    "favColor": "red"
    }

# Object

# Person constructor?
class Person:
    def __init__(self, name, age, favColor):
        self.name = name

# ex. output - print(person["name"])

## create instance of Person (use object)
person1 = Person(name= "Brandon", age= 24, favColor= "red")

# ex. output - print(person1.name)







