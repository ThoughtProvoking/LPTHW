# store a string
formatter = '{} {} {} {}'

# print the formatted string with four integers
print(formatter.format(1, 2, 3, 4))
# print the formatted string with four strings
print(formatter.format('one', 'two', 'three', 'four'))
# print the formatted string with four boolean values
print(formatter.format(True, False, False, True))
# print the formatted string with four of itself
print(formatter.format(formatter, formatter, formatter, formatter))
# print the formatted string with my own strings
print(formatter.format(
    'Life asked Death,',
    '"Why do people love me but hate you?",',
    'Death responded,',
    '"Because you are a beautiful lie and I am a painful truth."'
))
