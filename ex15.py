from sys import argv

# unpack the command line arguments
script, filename = argv

# open the provided file
txt = open(filename)

# print a string
print(f"Here's your file {filename}:")
# print the file contents
print(txt.read())

# close the file
txt.close()

# print a string
print("Type the filename again:")
# store the filename
file_again = input("> ")

# open the file
txt_again = open(file_again)

# print the file contents
print(txt_again.read())

# close the file
txt_again.close()
