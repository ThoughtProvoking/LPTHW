from sys import exit


def gold_room():
    print('This room is full of gold. How much do you take?')

    choice = input('> ')
    # bad check: 1a and similar cases cause error
    #if "0" in choice or "1" in choice:
    # better check: isnumeric() guarantees all characters are numeric
    # and at least one character given
    if choice.isnumeric():
        how_much = int(choice)
    else:
        dead('Man, learn to type a number.')

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead('You greedy bastard!')


def bear_room():
    print('There is a bear here.')
    print('The bear has a bunch of honey.')
    print('The fat bear is in front of another door.')
    print('How are you going to move the bear?')
    bear_moved = False

    while True:
        # split input by whitespace so strings like 'takehoney'
        # don't pass if-conditions
        choice = input('> ').split(' ')

        if 'honey' in choice:
            dead('The bear looks at you then slaps your face off.')
        elif 'taunt' in choice and not bear_moved:
            print('The bear has moved from the door.')
            print('You can go through it now.')
            bear_moved = True
        elif 'taunt' in choice and bear_moved:
            dead('The bear gets pissed off and chews your legs off.')
        elif 'door' in choice and bear_moved:
            gold_room()
        elif 'door' in choice and not bear_moved:
            print('The bear is in front of the door.')
        else:
            print('I got no idea what that means.')


def cthulhu_room():
    print('Here you see the great Cthulhu.')
    print('He, it, whatever stares at you and you go insane.')
    print('Do you flee for your life or eat your head?')
    
    # split input by whitespace so strings like 'headphone'
    # don't pass if-conditions
    choice = input('> ').split(' ')

    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead('Well, that was tasty!')
    else:
        cthulhu_room()


def dead(why):
    print(why, 'Good job!')
    exit(0)


def start():
    print('You are in a dark room.')
    print('There is a door to your right and left.')
    print('Which one do you take?')

    # split input by whitespace so strings like 'bright'
    # don't pass if-conditions
    choice = input('> ').split(' ')

    if 'left' in choice:
        bear_room()
    elif 'right' in choice:
        cthulhu_room()
    else:
        dead('You stumble around the room until you starve.')


start()
