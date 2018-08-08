name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
cmheight = 74 * 2.54
weight = 180 # lbs
kgweight = 180 * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"That's {round(cmheight)} in centimeters.")
print(f"He's {weight} pounds heavy.")
print(f"Which is {round(kgweight)} in kilograms.")
print("Actually that's not heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
