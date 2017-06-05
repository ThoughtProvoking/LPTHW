from sys import argv
from os.path import exists

# unpack command line arguments
script, from_file, to_file = argv

# print(f'Copy from {from_file} to {to_file}')

# # we could do these two in one line, how?
# # in_file = open(from_file)
# # indata = in_file.read()
# indata = open(from_file).read() # in one line

# print(f'The input file is {len(indata)} bytes long')
# print(f'Does the output file exists? {exists(to_file)}')
# print('Ready, hit RETURN to continue, CTRL-C to abort.')
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print('Alright, all done.')

# out_file.close()
# # in_file.close()

# reading and writing in one line
open(to_file, 'w').write(open(from_file).read())
