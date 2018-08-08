# Importing modules
from sys import argv
# Argv here
script, filename = argv

# Print statements
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# Don't know what this input saves as, oh it's a chance to press Ctrl + C or go ahead and continue script
input("?")
# Opening file
print("Opening the file...")
# Passing 'w' argument for the write option, truncates file with this option
target = open(filename, 'w')
# Truncate = totally erase that file, not needed with 'w' option
print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")
# Asks for 3 line inputs
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# Writes these into file with a blank space between each line
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
# Commented code out above to use 1 target.write line
target.write(f"{line1}\n{line2}\n{line3}\n")

# Close files here
print("And finally, we close it.")
target.close()