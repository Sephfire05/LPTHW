print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere this is none.
"""

print("---------------")
print(poem)
print("---------------")

five = 10 - 2 + 3 - 6
print(f'This should be five: {five}')

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates



start_point = 10000
# New variable names to save for later
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
# start point = 10000
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do this way:")
# formula = 1000 = secret_formula(start_point / 10)
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# unpack the formula arguments. beans, jars, crates so
# started = passed variable of (10000 / 10) = 1000 * 500 = 500000, 500000 / 1000 = 500, 500 / 100 = 5
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

