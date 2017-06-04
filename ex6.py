# set types_of_people to 10
types_of_people = 10
# set x to a f-string
x = f"There are {types_of_people} types of people."

# store a string
binary = "binary"
# store a string
do_not = "don't"
# set y to a f-string
y = f"Those who know {binary} and those who {do_not}." # 1st and 2nd string within a string

# print f-string stored in x
print(x)
# print f-string stored in y
print(y)

# print f-string within a f-string
print(f"I said: {x}") # 3rd string within a string
# print f-string within a f-string
print(f"I also said: '{y}'") # 4th string within a string

# set hilarious to False
hilarious = False
# store a string
joke_evaluation = "Isn't that joke so funny?! {}"

# print joke_evaluation string with hilarious variable
print(joke_evaluation.format(hilarious)) # not string within string: format() function is called

# store a string
w = "This is the left side of..."
# store a string
e = "a string with a right side."

# print two concatenated strings
print(w + e) # for strings, + means to concatenate (combine) the strings, not mathematical addition
