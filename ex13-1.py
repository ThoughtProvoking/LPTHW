from sys import argv

# unpack the command line arguments
script, name, age, height, weight = argv

# print each of the command line arguments
print(f'The script name: {script}')
print('Your name:', name)
print('Your age: {}'.format(age))
print('Your height: ' + height)
print(f'Your weight: {weight}')
