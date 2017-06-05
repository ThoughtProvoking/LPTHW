# create function called cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print amount of cheese
    print(f'You have {cheese_count} cheeses!')
    # print amount of crackers
    print(f'You have {boxes_of_crackers} boxes of crackers!')
    # print a string
    print("Man that's enough for a party!")
    # print a string
    print('Get a blanket.\n')

# print a string
print('We can just give the functions numbers directly:')
# call function with hard-coded integers
cheese_and_crackers(20, 30)

# print a string
print('OR, we can use variables from our script:')
# set amount_of_cheese to 10
amount_of_cheese = 10
# set amount_of_crackers to 50
amount_of_crackers = 50

# call function with integer variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print a string
print('We can even do math inside too:')
# call function with calculated values using hard-coded integers
cheese_and_crackers(10 + 20, 5 + 6)

# print a string
print('And we can combine the two, variables and math:')
# call function with calculated values using variables and hard-coded integers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# create a function called sum
def sum(x, y):
    # calculate and print the 'plus' of given arguments
    print(f'{x} + {y} = {x + y}')

# set x to 4
x = 4
# set y to 6
y = 6
# store a string
s1 = 'This string goes '
# store a string
s2 = 'with this string'

# call sum function 10 different ways, I think
# hard-coded integers
sum(3, 5)
# hard-coded strings
sum('one', 'two')
# arithmetic
sum(27328 / x, 34567 / y)
# integer variables
sum(x, x)
# string concatenation
sum('a' * x, 'b' * y)
# input and string concatenation
sum(input('x: ') * 4, input('y: ') * 2)
# string variables
sum(s1, s2)
# function call within function call
sum(len(s1), len(s2))
# formatted strings
sum(f'{x}', f'{y}')
# inputs
sum(input('x: '), input('y: '))
