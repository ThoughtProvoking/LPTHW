from sys import argv

# unpack the command line arguments
script, fruit = argv

# print the command line arguments
print('Script, {}, ran'.format(script))
print('Fruit given:', fruit)

# ask for another input
another_fruit = input('Another fruit please? ')
# print the user input
print('You also gave:', another_fruit)
