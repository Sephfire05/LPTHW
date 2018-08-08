# function cheese_and_crackers( argument1, argument2): 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Formatted print
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# Call function with these values
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# Variables here for set values
amount_of_cheese = 10
amount_of_crackers = 50
# Call function with these stored variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# Doing math inside, comma still separating values
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# Combination of variables and values (basic math)
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)