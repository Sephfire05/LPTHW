# Modules, Classes, and Objects

# Using Classes, you can add consistency to your programs so they can be used in a cleaner way
# Object-oriented programming (OOP)

# Modules are like Dictionaries
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# A class is like a mini-module
# instantiate (create) a class by calling the class like it's a function, example
thing = MyStuff()  #Instantiate here
thing.apple()
print(thing.tangerine)

# Order of sequence, behidn the scenes
# Python looks for MyStuff() and see that it's a class you've defined
# Python crafts an empty object with all the functions you've defined (def)
# Python looks to see if you've made that magic "__init__" functions and it calls that function
# to initialize newly created empty object
# the __init__ gets an extra variable, self, and you can set variables in it
# self.tangerine sets the self to a song lyric
# newly minted object and assigns it ot the thing variable for you to work with

# Uses the class as a blueprint for building a copy of that thing

