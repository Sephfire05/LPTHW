print("Mary had a little lamb.")
#the 'snow' is a string that fills the empty f-string placeholder
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) #what'd that do?
#It prints the . 10 times.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
#These are string concatenations with a space after end6
#watch that comma at the end. try removing it and see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
#the comma after end6 indicates the end of the concatenation and makes a space at the end with end=' '
