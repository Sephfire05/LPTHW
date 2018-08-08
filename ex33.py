# While Loops
# While loops keep looping until false
# Use them sparingly, use for more often
# Read your while loop and make sure it will be false at some point
# print out the test variable and the top and bottom to see what it's doing
# Start counter here, outside of loops
i = 0
numbers = [] # empty array list
numinput = int(input("> "))

while i in range(i, numinput): # will be after 5
    print(f"At the top i is {i}") # Start at 0
    numbers.append(i) # append the number to the list
 # Counter + 1
    i += 2
    print("Numbers now: ", numbers) # prints the list out
    print(f"At the bottom i is {i}") 


print("The numbers: ")
# This statement prints the elements of the list after the while loop has been completed
for num in numbers:
    print(num)