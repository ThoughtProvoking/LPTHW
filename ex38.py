# set ten_things to string of 6 whitespace separated words
ten_things = "Apple Orange Crows Telephone Light Sugar"

# print string
print("Wait, there are not 10 things in that list. Let's fix that.")

# split ten_things into list delimited by whitespace
# split(ten_strings, ' ')
stuff = ten_things.split(' ')

# set more_stuff to list of 8 strings
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# while stuff has less than 10 items
while len(stuff) < 10:
    # get last item from more_stuff
    # pop(more_stuff)
    next_one = more_stuff.pop()
    # print what it is
    print('Adding: ', next_one)
    # append it to stuff
    # append(stuff, next_one)
    stuff.append(next_one)
    # print new length of stuff
    print(f'There are {len(stuff)} items now.')

# print resulting stuff
print('There we go: ', stuff)

# print string
print("Let's do some things with stuff.")

# print the second item in stuff
print(stuff[1])
# print the last item in stuff
print(stuff[-1]) # whoa! fancy
# remove and return the last item in stuff
# pop(stuff)
print(stuff.pop())
# join all items of stuff with whitespace into a string
# join(' ', stuff)
print(' '.join(stuff)) # what? cool!
# join items from indices 3 to (not including) 5 with octothorpe into a string
# join('#', stuff[3:5])
print('#'.join(stuff[3:5])) # super stellar
