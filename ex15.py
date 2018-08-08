from sys import argv
# Imported argv module
script, filename = argv
# Open the txtfile name as txt variable
txt = open(filename)

# Reprints the filename argument
print(f"Here's your file {filename}:")
# open.read(filename) command. The .read is a command to the file
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

# Rereading this txt file
txt_again = open(file_again)
# Print out the file
print(txt_again.read())