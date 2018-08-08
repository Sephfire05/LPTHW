# this one is like your scripts with argv
def print_two(*args): # the * is for unpacking arguments and a : at end to define the function
    arg1, arg2 = args #four indented spaces to indicate part of function
    print(f"arg1: {arg1}, arg2: {arg2}")

    
# ok, that's *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# Function checklist
# def function_name(argument1, argument2, separated, by, commas):
#   start at 4 spaces or a tab
# end the function with unindented lines

# call of a function by 
# function_name(argument, argument2)
