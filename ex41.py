# class - Tell Python to make a new type of thing
# object - the most basic type of thing, and any instance of some thing
# instance - What you get when you tell Python to create a class
# def - how to define a function inside a class
# self - inside the functions in a class, self is a variable for the instance/object being assessed
# inheritance - the concept that one class can inherit traits from another class, like you and your parents
# composition - the concept that a class can be composed of other classes as parts, like a car having wheels
# attribute - a property classes have that are from composition and are usually variables
# is-a - a phrase to say that something inherits from another, as in 'salmon' is-a 'fish'
# has-a - a phrase to say that something is composed of other things or has a trait, as in 'salmon' has-a 'mouth'

# class X(Y)
# make a class named X that is-a Y
#
# class X(object): def __init__(self, J)
# class X has-a __init__ that takes self and J parameters
#
# class X(object): def M(self, J)
# class X has-a function named M that takes self and J parameters
#
# foo = X()
# set foo to an instance of class X
#
# foo.M(J)
# from foo, get the function M, and call it with parameters self, J
#
# foo.K = Q
# from foo, get the K attribute and set it to Q
