# String with placeholders
formatter = "{} {} {} {}"
# Put these in the placeholders of formatter
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# This puts those 4 {} 4 times so 16 {} 
print(formatter.format(formatter, formatter, formatter, formatter))
# A poem here, all one line with no \n characters for empty lines.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))