# \t indicates a tab
tabby_cat = "\tI'm tabbed in."
# \n indicate a new line
persian_cat = "I'm split\non a line."
# A regular \ indicates the next character is a literal string value
backslash_cat = "I'm \\ a \\ cat."
test_cat = "Let's try out some new escape sequences"
escape_cat = "This is an exa:\vmple."
#\f formfeed, next line same place

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
""" #the \n\t is another way of creating another list ish component

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(test_cat)
print(escape_cat)
