from sys import argv

# unpack the command line arguments
script, user_name, age = argv
# store the input prompt
prompt = 'Distracting prompt \N{BLACK HEART}> '

# print a greeting
print(f"Hi {user_name}, I'm the {script} script.")
# print a string
print("I'd like to ask you a few questions.")
# ask a question
print(f"Do you like me {user_name}?")
# store the answer
likes = input(prompt)

# ask another question
print(f"Where do you live {user_name}?")
# store the answer
lives = input(prompt)

# print a question
print(f"What kind of computer do you have?")
# store the answer
computer = input(prompt)

# print all of the inputs together
print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You're {age} years old.
And you have a {computer} computer. Nice.
''')
