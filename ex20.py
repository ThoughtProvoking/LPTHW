from sys import argv

# unpack command line arguments
script, input_file = argv

# create function with one argument
def print_all(f):
    # print all file contents
    print(f.read())

# create function with one argument
def rewind(f):
    # place pointer back to first character
    f.seek(0)

# create function with two arguments
def print_a_line(line_count, f):
    # print line number and a line from file
    print(line_count, f.readline())

# open file
current_file = open(input_file)

# print a string
print("First let's print the whole file:\n")

# call function to print all file content
print_all(current_file)

# print a string
print("Now let's rewind, kind of like a tape.")

# call function to return pointer to beginning of file
rewind(current_file)

# print a string
print("Let's print three lines:")

# set current_line to 1
current_line = 1
# call function to print first line of file
print_a_line(current_line, current_file) # current_line = 1

# increment current_line by 1
current_line += 1
# call function to print second line of file
print_a_line(current_line, current_file) # current_line = 2

# increment current_line by 1
current_line += 1
# call function to print third line of content
print_a_line(current_line, current_file) # current_line = 3
