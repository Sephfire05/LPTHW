#int var
types_of_people = 10
#f-string = string with a format in there of types of people = 10
x = f"There are {types_of_people} types of people."
#string values
binary = "binary"
do_not = "don't"
#f-string
y = f"Those who know {binary} and those who {do_not}."

#print out those f-strings
print(x)
print(y)

#prints strings and the f-strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

#boolean value
hilarious = False
#empty place holder
joke_evaluation = "Isn't that joke so funny?! {}"

#formatted string with .format syntax. The placeholder is that boolean value of False
print(joke_evaluation.format(hilarious))

#Simple strings
w = "This is the left side of..."
e = "a string with a right side."
#String concatenation 
print(w + e)