from sys import argv

# unpack command line arguments
script, filename = argv

# open file
txt = open(filename)

# print a formatted string
print(f"The file contents of '{filename}':")
# print file content
print(txt.read())

# close file
txt.close()
