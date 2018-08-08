# IS-A, HAS-A, Objects, and Classes
# is-a - objects and classes being related to each other by a class relationship
# has-a - talk about objects and classes that are related only because they reference each other

# replace each ##?? with a comment that says whether the next list represents an is-a or
# a has-a relatinoships and what that relationship is

## Animal is-a object
class Animal(object):
    pass

## ?? - Dog is a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ?? 2 params, self and name
        self.name = name

## ?? - Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## ?? - Person is a object
class Person(object):

    def __init__(self, name):
        ## ?? - 
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## ?? - Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ?? - Fish is-a object
class Fish(object):
    pass

## ?? - Salmon is a Fish
class Salmon(Fish):
    pass

## ?? - Halibut is a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## ?? - Satan is a Cat
satan = Cat("Satan")

## ?? - Mary is a Person
mary = Person("Mary")

## ?? - satan is 
mary.pet = satan

## ??
frank = Employee("Frank", 120000) # frank is an instance of Employee (params)

## ?? class.command = rovers
frank.pet = rover

## ?? flipper is an instance of Fish
flipper = Fish()

## ?? crouse is an instance of Salmon
crouse = Salmon()

## ?? harry is an instance of Halibut
harry = Halibut()