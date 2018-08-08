print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end= ' ')
weight = input()

print(f"So, you're {age} years old, {height} tall and {weight} lbs heavy.")

age2 = int(input("Enter someone else's age: "))
height2 = int(input("Enter someone else's height in cm: "))
weight2 = int(input("Enter someone else's weight in lbs: "))

#f string format with int inputs
status2 = "So, they are {} years old, {} cm tall and {} lbs heavy."

print(status2.format(age2,height2,weight2))