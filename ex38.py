# Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]
    
while len(stuff) != 10:
    next_one = more_stuff.pop() # adds the last element of more_stuff and takes it off the list
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # Prints second element
print(stuff[-1]) # whoa! fancy, printed out the last element
print(stuff.pop()) # Get rid of the last element
print(' '.join(stuff)) #what? cool - Prints off list with spaces between elements
print('#'.join(stuff[3:5])) # super stellar - Prints off element 3 and 4 with a # between. Item 4 and 5, not 6 (element 5)

# When To Use Lists
# Use a list whenever you have something that matches the list data structure's useful features
# Examples
#  1. If you need to maintain order
#  2. If you need to access the contents randomly by a number
#  3. If you need to go through the contents linearly (first to last) - for loops