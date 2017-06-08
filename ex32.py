the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f'This is count {number}')

# same as above
for fruit in fruits:
    print(f'A type of fruit: {fruit}')

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f'I got {i}')

# # we can also build lists, first start with an empty one
# elements = []

# # then we use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print(f'Adding {i} to the list.')
#     # append is a function that lists understand
#     elements.append(i)
#
# avoiding unnecessary code
elements = range(0, 6)

# now we can print them out too
for i in elements:
    print(f'Element was: {i}')

# Other list operations:
#   extend(iterable) - extends list by appending all elements in iterable
#   insert(i, x) - insert x at index i
#   remove(x) - remove first element equal to x
#   pop([i]) - pop last element or item at index i
#   clear() - empties list
#   index(x[,start[,end]]) - return index of first instance of x
#   count(x) - return occurrence of element x in list
#   sort() - in-place sort of list
#   reverse() - in-place reverse of order of elements
#   copy() - return shallow copy of list
