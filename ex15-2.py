filename = input("Input the file you would like to open: ")

txt = open(filename)
print(f"Here's your file {filename}:") #Remember to put f" for using {} in strings and print statements.
print(txt.read())