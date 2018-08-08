# Learning to Speak Object-Oriented

# Vocabulary
# class - Tells python to make a new type of thing
# object - 2 meanings: the most basic type of thing, any instance of some thing
# instance - What you get when you tell Python to create a class
# def - how you define a function inside a class
# self - inside the functions in a class, self is a variable for the instance/object being accessed
# inheritance - One class can inherit traits from another class (parents and children)
# composition - A Class can be composed of other classes as parts, (car with wheels)
# attribute - A property classes have that are from composition and are suually variables
# is-a - A phrase to say that something inherits from another
# has-a - A phrase to say that somethign is composed of other things or has a trait

# Phrase Drills
# classX(Y) - Make a class named X that is-a Y
# class X(object): def __init__(self, J) - Class X has-a init that takes self and J parameters
# class X(object): def M(self, J) - class X has a function named M that takes self and J parameters
# foo = X() - Set foo to an instance of class X
# foo.M(J) - from foo get the M function and call it with parameters self, J
# foo.K = Q - From foo, get the K attribute and set it to Q

# A Reading Test
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    # each triple sect gets replaced
    "class %%%(%%%):": # key 
     "Make a class named %%% that is-a %%%.", # value
    "class %%%(object):\n\tdef __init__(self, ***)" :
     "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
     "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'."
     # 6 types of questions
}

# do they want to drill phrases first
# argument should look like python ex41.py english | 2 args
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines(): # opens url and reads them
    WORDS.append(str(word.strip(), encoding="utf-8")) # adds words to the list

def convert(snippet, phrase): # function convert (arg1, arg2)
    class_names = [w.capitalize() for w in # Capitalize class names
                   random.sample(WORDS, snippet.count("%%%"))] # random sample from WORDS list
                   # snippet.count these two triple sects
    other_names = random.sample(WORDS, snippet.count("***"))
    results = [] # claim empty list
    param_names = []
# 0, range of the @@@
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3) # param_count = 1, 2, 3
        param_names.append(', '.join( # sets the parameter names with a comma separation
            random.sample(WORDS, param_count))) # with these samples of WORDS list, 
        
    for sentence in snippet, phrase:
        result = sentence[:] # result = sentence list from first to last

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    
    return results

# keep going until they try CTRL-D
try: # try this code block
    while True: # infinite loop
        snippets = list(PHRASES.keys()) # list of dict keys (questions)
        random.shuffle(snippets) # random shuffle of questions

        for snippet in snippets:
            phrase = PHRASES[snippet] # phrase = keys value
            question, answer = convert(snippet, phrase) # tuple = function results
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")