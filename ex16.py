from sys import argv

# unpack command line arguments
script, filename = argv

# ask for confirmation
# print a formatted string
print(f"We're going to erase {filename}.")
# print a string
print("If you don't want that, hit CTRL-C (^C).")
# print a string
print("If you do want that, hit RETURN.")

# receive user input, don't store it
input("?")

# print a string
print("Opening the file...")
# open file
# need 'w' argument because it overwrites existing content
# which may not be user's intention.
target = open(filename, 'w')

# not necessary because opening file with 'w' automatically truncates it
# print a string
print("Truncating the file. Goodbye!")
# delete all file content
target.truncate()

# print a string
print("Now I'm going to ask you for three lines.")

# ask for and store user's three lines of choice
# store user input
line1 = input("line 1: ")
# store user input
line2 = input("line 2: ")
# store user input
line3 = input("line 3: ")

# print a string
print("I'm going to write these to the file.")

# write user's given lines into file each ending with linefeed character
# # write into file
# target.write(line1)
# # write into file
# target.write('\n')
# # write into file
# target.write(line2)
# # write into file
# target.write('\n')
# # write into file
# target.write(line3)
# # write into file
# target.write('\n')
# shorten write into one line
target.write(f"{line1}\n{line2}\n{line3}\n")

# print a string
print("And we finally close it.")
# close the file
target.close()
