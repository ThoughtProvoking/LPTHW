from sys import argv
# read the WYSS section for how to run this

# unpack the command line arguments (expecting 4)
#
# ValueError: not enough values to unpack (expected 4, got 3)
#   User did not give enough command line arguments. User gave 3,
#   but the script expected 4.
#
# ValueError: too many values to unpack (expected 4)
#   User gave too many command line arguments, but the script only needs 4.
script, first, second, third = argv

# print the name of the script called
print('The script is called:', script)
# print the first argument
print('Your first variable is:', first)
# print the second argument
print('Your second variable is:', second)
# print the third argument
print('Your third variable is:', third)
