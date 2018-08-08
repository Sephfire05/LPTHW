# Import argv module
from sys import argv
# These are the arguments 
script, input_file = argv
# This prints the current file through .read command to f (passed argument)
def print_all(f):
    # .read reada all like a text file
    print(f.read())
# This rewinds the file? .seek puts the file in the indicated position
def rewind(f):
    f.seek(0) #indicated position of 0 (beginning) byte.

def print_a_line(line_count, f): # arguments here
    # line_count is a python reserved function, positional argument here
    print(line_count, f.readline()) #line_count and read line
    

current_file = open(input_file) 

print("First let's print the whole file:\n")

# Prints the file
print_all(current_file)

# File stays open
print("Now let's rewind, kind of like a tape.")

# rewind puts the file back in beginning
rewind(current_file)

print("Let's print three lines:")

# Positional arguments here for line_count and print_a_line function
# First position of line count = 1
current_line = 1
print_a_line(current_line, current_file)
# Second position of line count = 2
current_line += 1
print_a_line(current_line, current_file)
# Third position of line count = 3
current_line += 1 # += means current_line = current_line + 1
print_a_line(current_line, current_file)
