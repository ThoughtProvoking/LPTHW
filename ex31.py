# print multi-line string
print('''You enter a dark room with two doors.
Do you go through door #1 or door #2?''')

# store user input
door = input('> ')

if door == '1': # door #1
    print("There's a giant bear here eating a cheese cake.")
    print('What do you do?')
    print('1. Take the cheese cake.')
    print('2. Scream at the bear.')

    # store user input
    bear = input('> ')

    if bear == '1': # 1. Take the cheese cake
        print('The bear eats your face off. Good job!')
    elif bear == '2': # 2. Scream at the bear
        print('The bear eats your legs off. Good job!')
    else: # everything else
        print(f'Well, doing {bear} is probably better.')
        print('Bear runs away.')

elif door == '2': # door #2
    print("You stare into the endless abyss of Cthulu's retina")
    print('1. Blueberries.')
    print('2. Yellow jacket clothespins.')
    print('3. Understanding revolvers yelling melodies.')

    # store user input
    insanity = input('> ')

    if insanity == '1' or insanity == '2':
        # 1. Blueberries or 2. Yellow jacket clothespins
        print('Your body survives powered by a mind of jello.')
        print('Good job!')
    else: # 3. Understanding revolvers yelling melodies or everything else
        print('The insanity rots your eyes into a pool of muck.')
        print('Good job!')

else: # no door
    #print('You stumble around and fall on a knife and die. Good job!')
    print('You stumble around and fall down a hole.')
    print('At the bottom, you see two buttons.')
    print('Do you press button #1 or button #2?')

    button = input('> ')

    if button == '1':
        print('A giant boulder falls and crushes you. Good job!')
    elif button == '2':
        print('Poisonous gas is released and you die. Good job!')
    else:
        print('With no sustenance in sight, you die of hunger. Good job!')
