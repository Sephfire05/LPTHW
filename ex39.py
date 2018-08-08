# Dictionaries, Oh Lovely Dictionaries
# Dictionary data structure in Python {}
# Can be used as a database
# key : value
# access by stuff[key]

# create a mapping of state to abbreviation

states = {                    # Notice how each one is in a key : value
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York' # cities[key] = value
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10) # ------------
print("NY State has: ", cities['NY']) # print out values by dict[key]
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan']) 
print("Florida abbreviation is: ", states['Florida']) # states dict Florida key

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']]) #cities dict, states key, michigan values
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
# rolls through all the dict and gives values in list form
for state, abbrev in list(states.items()): #x, y in the states items value
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
# goes through every key in cities in list form
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()): # key, value
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}") # Call cities dict, abbrev column value

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas') # Looks for this key, should give False

if not state: # if this statement is True
    print("Sorry, no Texas.")

# get a city with a default value
# looking at cities dict - .get command (value, default value if not found)
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}") # Returns that default value 'DNE'

# What Dictionaries Can Do
# Another example of a data structure, most commonly used data structures in programming
# matching items to other items keys to values
# look-up tables
# Use a list for sequence of things that needs to be in order, and you only need to look them up
# by numeric index

# To order a dictionary 
# collections.OrderedDict