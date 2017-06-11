## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self, name):
        ## Animal has-a name
        self.name = name

    ## Animal has-a eat function
    def eat(self, food):
        print(f'{self.name} is eating {food}.')


## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name


## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name


## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    ## Person has-a play_with_pet function
    def play_with_pet(self):
        print(f'{self.name} is playing with their pet, {self.pet.name}.')


## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name; hmm what is this strange magic?
        # calling parent class (person) __init__ with name argument
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        ## Employee has-many jobs
        self.job = []

    ## Employee has-a buy function
    def buy(self, stuff):
        print(f'{self.name} bought {stuff}.')

## Fish is-a object
class Fish(object):
    
    def __init__(self, name):
        ## Fish has-a name
        self.name = name

    ## Fish has-a swim function
    def swim(self):
        print(f'{self.name} is swmming...')


## Salmon is-a Fish
class Salmon(Fish):
    
    def __init__(self, name):
        ## Salmon has-a name
        super(Salmon, self).__init__(name)


## Halibut is-a Fish
class Halibut(Fish):
    
    def __init__(self, name):
        ## Halibut has-a name
        super(Halibut, self).__init__(name)


## rover is-a dog
rover = Dog('Rover')
rover.eat('kibbles')

## satan is-a cat
satan = Cat('Satan')
satan.eat('fish')

## mary is-a person
mary = Person('Mary')
# Person cannot call Employee functions/attributes
#mary.buy('soap')
#print(mary.salary)

## mary has-a pet cat, satan
mary.pet = satan
mary.play_with_pet()

## frank is-a employee and has-a salary 120,000
frank = Employee('Frank', 120000)
frank.buy('milk')

## frank has-a pet dog, rover
frank.pet = rover
frank.play_with_pet()

## flipper is-a fish
flipper = Fish('Flipper')
flipper.swim()

## crouse is-a salmon
crouse = Salmon('Crouse')
crouse.swim()

## harry is-a halibut
harry = Halibut('Harry')
harry.swim()

# 1.) in Python 2, without explicit object inheritance,
#       the code used an old-style class which caused some code to act differently
#       such as type() returning <type 'instance'> instead of <type '__init__.Foo'>.
#       Old-style classes no longer exist, as of Python 3.
# 2.) yes, everything in Python is an object
# 3.) Parent class cannot call child class attributes/functions, 
#       but children class can call parent class attributes/functions
# 5.) is-many inheritance is denoted by comma separated class names during class definition:
#       class Dog(Animal, Canine): <--- Dog is-a Canine is-a Animal
