# Importing argv from sys for arguments
from sys import argv
# These are called modules or libraries
# argv is called the argument variable
# This variable holds your arguments to pass to Python

# read the WYSS section for how to run this
# Script is the argument 0 or name of script
# Each subsequent argument after are the variables passed down to the Python script
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is called:", first)
print("Your second variable is called:", second)
print("Your third variable is called:", third)

