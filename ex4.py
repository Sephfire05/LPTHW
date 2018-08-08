#Int
cars = 100
#Floating point number
space_in_a_car = 4.0
#int
drivers = 30
#int
passengers = 90
#This variable is a function 100 - 30 = 70
cars_not_driven = cars - drivers
#int = 30
cars_driven = drivers
#Function = 30 * 4.0 = 120.0 floating point number
carpool_capacity = cars_driven * space_in_a_car
#function = 90 / 30 = 3.0 (4 spaces - 1 driver = 3.0)
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")