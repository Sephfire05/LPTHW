from sys import argv
from os.path import exists
# Importing modules
# exists just sees if this file exists
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line. how?
in_file = open(from_file)
indata = in_file.read()
# in_file = open(from_file).read() should work as one line
# .read is the command to the open function
print(f"The input file is {len(indata)} bytes long")
# Prints the file size
print(f"Does the output file exist? {exists(to_file)}")
print("Read, hit RETURN to continue , CTRL-C to abort.")
input()
# The exists just passes a TRUE or FALSE

# These two lines opens the to_file, truncates / writes to it, and writes the in_files contents
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
# Closes the two files 
out_file.close()
in_file.close()
# Try to write this script as short as you can