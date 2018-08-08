from sys import argv

script, filename = argv

print(f"Now we're going to read {filename}")
print("Here it goes.")

txt = open(filename)

print(txt.read())
