from sys import argv # add import

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() # add this line
print("How much do you weigh?", end=' ') # add end parentheses
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename) # fix variable name filenme

print(f"Here's your file {filename}:") # add f before string
print(txt.read()) # fix variable name tx

txt.close() # add this line

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) # replace _ with .

txt_again.close() # add this line

print('Let\'s practice everything.') # add escape sequence for single-quote character 
      # or change to double-quote string
      # or use triple single/double-quote string
print('You\'d need to know \'bout escapes\
      with \\ that do: \n newlines and \t tabs.') # add backslash to denote multi-line string
      # or use another print()
      # or use triple single/double-quote string
      # or combine into one print()

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # add end double-quote
print(poem)
print("--------------") # add beginning double-quote


five = 10 - 2 + 3 - 6 # add integer (6)
print(f"This should be five: {five}") # add end parentheses

def secret_formula(started): # add colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # add slash symbol
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # add crates variable

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # fix variable name startpoint
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 # fix variable name cates
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") # add functional parentheses around string

if people > cats: # replace < with >
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: # add colon
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: # add colon
    print("People are less than or equal to dogs.") # add end double-quote


if people == dogs: # replace = with ==
    print("People are dogs.")

