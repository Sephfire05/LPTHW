def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# These are the numbers that should come out.
# age = 35, height = 74, weight = 180, iq = 50
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
# Start from innermost equation
# iq = 50 divide(50, 20) return 2.5 multiply(180, 2.5) return 450, subtract( 74 - 450) return
# return -376, add (35 + -376) return what = -341
what = add(age, subtract(height, multiply(weight, divide(iq, 20))))
# W00T w00t! Got it right on the first try!
print("That becomes: ", what, "Can you do it by hand?")