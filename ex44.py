#------ Inheritance ------#

# a class called Parent
class Parent(object):

    # demonstrates implicit function call for children classes
    def implicit(self):
        # print message
        print('PARENT implicit()')

    # demonstrates override function call for children classes
    def override(self):
        # print message
        print('PARENT override()')

    # demonstrates altered function call for children classes
    def altered(self):
        # print message
        print('PARENT altered()')


# a class called Child that inherits from (is-a) Parent
class Child(Parent):

    # constructor
    def __init__(self, stuff):
        # set Child attribute
        self.stuff = stuff
        # call parent constructor
        super(Child, self).__init__()
    
    # override parent function
    def override(self):
        # print message
        print('CHILD override()')

    # override and modify parent function
    def altered(self):
        # print message
        print('CHILD, BEFORE PARENT altered()')
        # call parent altered()
        super(Child, self).altered()
        # print message
        print('CHILD, AFTER PARENT altered()')


# create Parent and Child object
dad = Parent()
son = Child("stuff")

# call Parent and Child implicit function
dad.implicit()
son.implicit()

# call Parent and Child override function
dad.override()
son.override()

# call Parent and Child altered function
dad.altered()
son.altered()


#------ Composition ------#

# a class called Other
class Other(object):

    # demonstrate override function call
    def override(self):
        # print message
        print('OTHER override()')

    # demonstrate implicit function call
    def implicit(self):
        # print message
        print('OTHER implicit()')

    # demonstrate altered function call
    def altered(self):
        # print message
        print('OTHER altered()')


# a class called Child
class Child(object):

    # constructor
    def __init__(self):
        # Child has-a Other
        self.other = Other()

    # implicit Other function
    def implicit(self):
        # call Other implicit function
        self.other.implicit()

    # override Other function
    def override(self):
        # print message
        print('CHILD override()')

    # override and modify Other function
    def altered(self):
        # print message
        print('CHILD, BEFORE OTHER altered()')
        # call Other altered function
        self.other.altered()
        # print message
        print('CHILD, AFTER OTHER altered()')


# create Child object
son = Child()

# call Child functions
son.implicit()
son.override()
son.altered()
