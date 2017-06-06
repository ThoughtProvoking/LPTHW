# print a string
print("Let's practice everything.")
# print a string with escape sequences
print('You\'d need to know \'bout escapes with \\ that do:')
# print a string with escape sequences
print('\n newlines and \t tabs.')

# store a multi-line string with escape sequences
poem = '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
'''

# print a string
print('--------------')
# print poem variable
print(poem)
# print a string
print('--------------')

# set five to an calculates value (=5)
five = 10 - 2 + 3 - 6
# print result in f-string
print(f'This should print five: {five}')

# create function with one argument
def secret_formula(started):
    # started multiply by 500 and store into jelly_beans
    jelly_beans = started * 500
    # jelly_beans divide by 1000 and store into jars
    jars = jelly_beans / 1000
    # jars divide by 100 and store into crates
    crates = jars / 100
    # return list of three variables
    return jelly_beans, jars, crates


# set start_point to 10000
start_point = 10000
# call secret_formula function and store into returned values into separate variables
beans, jars, crates = secret_formula(start_point)

# remember this is another way to format a string
# print start_point in formatted string using .format()
print('With a starting point of: {}'.format(start_point))
# it's just like with a f"" string
# print results in f-string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# start_point divide by 10 and store back into itself
start_point /= 10

# print a string
print('We can also do that this way:')
# call secret_formula function and store into list
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# print formatted string using list
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
