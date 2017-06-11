from sys import exit
from random import randint
from textwrap import dedent


# Parent class for all of the scenes
class Scene(object):

    # default enter function, will run if child class does not implement
    def enter(self):
        print('This scene is not yet configured.')
        print('Subclass it and implement enter().')
        exit(1)


# Engine class, will actually start the game
class Engine(object):

    def __init__(self, scene_map):
        # scene_map is-a Map
        self.scene_map = scene_map

    # begins the game
    def play(self):
        # get the opening (first) scene
        current_scene = self.scene_map.opening_scene()
        # get the last scene
        last_scene = self.scene_map.next_scene('finished')

        # game scene progression is linear, so loop until last scene
        while current_scene != last_scene:
            # get the name of the next scene after interacting with current scene
            # the return statement gives the next scene name
            next_scene_name = current_scene.enter()
            # set current_scene [object] to next_scene [object]
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        # because loop exits before enter() of finished scene is called
        current_scene.enter()


# the scene when user dies
class Death(Scene):

    # list of possible death quips
    quips = [
        'You died. You kinda suck at this.',
        'Your Mom would be proud...if she were smarter.',
        'Such a luser.',
        "I have a small puppy that's better than this.",
        "You're worse than your Dad's jokes."
    ]

    # override enter()
    def enter(self):
        # print a random death quip
        print(Death.quips[randint(0, len(self.quips) - 1)])
        # exit the program
        exit(1)


# central corridor scene (starting/first scene)
class CentralCorridor(Scene):

    # override enter()
    def enter(self):
        # print description of game setting and scene
        print(dedent("""
             The Gothons of Planet Percal #25 have invaded your ship and
             destroyed your entire crew.  You are the last surviving
             member and your last mission is to get the neutron destruct
             bomb from the Weapons Armory, put it in the bridge, and
             blow the ship up after getting into an escape pod.

             You're running down the central corridor to the Weapons
             Armory when a Gothon jumps out, red scaly skin, dark grimy
             teeth, and evil clown costume flowing around his hate
             filled body.  He's blocking the door to the Armory and
             about to pull a weapon to blast you.
             """))

        # take user input
        action = input('> ').split(' ')

        # if user wants to shoot, user dies
        if 'shoot' in action:
            print(dedent("""
                  Quick on the draw you yank out your blaster and fire
                  it at the Gothon.  His clown costume is flowing and
                  moving around his body, which throws off your aim.
                  Your laser hits his costume but misses him entirely.
                  This completely ruins his brand new costume his mother
                  bought him, which makes him fly into an insane rage
                  and blast you repeatedly in the face until you are
                  dead.  Then he eats you.
                  """))
            return 'death'

        # if user wants to dodge, user dies
        elif 'dodge' in action:
            print(dedent("""
                  Like a world class boxer you dodge, weave, slip and
                  slide right as the Gothon's blaster cranks a laser
                  past your head.  In the middle of your artful dodge
                  your foot slips and you bang your head on the metal
                  wall and pass out.  You wake up shortly after only to
                  die as the Gothon stomps on your head and eats you.
                  """))
            return 'death'

        # if user tells a joke, user lives
        elif 'joke' in action:
            print(dedent("""
                  Lucky for you they made you learn Gothon insults in
                  the academy.  You tell the one Gothon joke you know:
                  Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                  fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
                  not to laugh, then busts out laughing and can't move.
                  While he's laughing you run up and shoot him square in
                  the head putting him down, then jump through the
                  Weapon Armory door.
                  """))
            return 'laser_weapon_armory'

        # replay scene if action is not defined
        else:
            print('DOES NOT COMPUTE')
            return 'central_corridor'


# laser weapon armory scene (second scene)
class LaserWeaponArmory(Scene):

    # override enter()
    def enter(self):
        # print scene description
        print(dedent("""
              You do a dive roll into the Weapon Armory, crouch and scan
              the room for more Gothons that might be hiding.  It's dead
              quiet, too quiet.  You stand up and run to the far side of
              the room and find the neutron bomb in its container.
              There's a keypad lock on the box and you need the code to
              get the bomb out.  If you get the code wrong 10 times then
              the lock closes forever and you can't get the bomb.  The
              code is 3 digits.
              """))
        
        # generated random three-digit code
        code = '000' # cheating, f'{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}'
        # store user input
        guess = input('[keypad]> ')
        # set guess attempts to 0
        guesses = 1

        # loop while guess is incorrect and user still has less than 10 attempts
        # allowed 11 guesses because the guess above was not accounted for, so
        # guesses has to start at 1 or change conditional to guesses < 9
        while guess != code and guesses < 10:
            print('BZZZZEDDD!')
            guesses += 1
            guess = input('[keypad]> ')

        # if guess is correct, user lives
        if guess == code:
            print(dedent("""
                  The container clicks open and the seal breaks, letting
                  gas out.  You grab the neutron bomb and run as fast as
                  you can to the bridge where you must place it in the
                  right spot.
                  """))
            return 'the_bridge'

        # otherwise, user dies
        else:
            print(dedent("""
                  The lock buzzes one last time and then you hear a
                  sickening melting sound as the mechanism is fused
                  together.  You decide to sit there, and finally the
                  Gothons blow up the ship from their ship and you die.
                  """))
            return 'death'


# the bridge scene (third scene)
class TheBridge(Scene):

    # override enter()  
    def enter(self):
        # print scene description
        print(dedent("""
              You burst onto the Bridge with the netron destruct bomb
              under your arm and surprise 5 Gothons who are trying to
              take control of the ship.  Each of them has an even uglier
              clown costume than the last.  They haven't pulled their
              weapons out yet, as they see the active bomb under your
              arm and don't want to set it off.
              """))

        # take user input
        action = input('> ').split(' ')

        # if user wants to throw the bomb, user dies
        if 'throw' in action:
            print(dedent("""
                  In a panic you throw the bomb at the group of Gothons
                  and make a leap for the door.  Right as you drop it a
                  Gothon shoots you right in the back killing you.  As
                  you die you see another Gothon frantically try to
                  disarm the bomb. You die knowing they will probably
                  blow up when it goes off.
                  """))
            return 'death'

        # if user slowly places the bomb, user lives
        elif 'place' in action:
            print(dedent("""
                  You point your blaster at the bomb under your arm and
                  the Gothons put their hands up and start to sweat.
                  You inch backward to the door, open it, and then
                  carefully place the bomb on the floor, pointing your
                  blaster at it.  You then jump back through the door,
                  punch the close button and blast the lock so the
                  Gothons can't get out.  Now that the bomb is placed
                  you run to the escape pod to get off this tin can.
                  """))
            return 'escape_pod'

        # replay scene if action is not defined
        else:
            print('DOES NOT COMPUTE')
            return 'the_bridge'


# escape pod scene (fourth scene)
class EscapePod(Scene):

    # override enter()
    def enter(self):
        # print scene description
        print(dedent("""
              You rush through the ship desperately trying to make it to
              the escape pod before the whole ship explodes.  It seems
              like hardly any Gothons are on the ship, so your run is
              clear of interference.  You get to the chamber with the
              escape pods, and now need to pick one to take.  Some of
              them could be damaged but you don't have time to look.
              There's 5 pods, which one do you take?
              """))
            
        # generate a random pod number
        good_pod = 0 # cheating, randint(1, 5)
        # take user input
        guess = input('[pod #]> ')

        # if guess is incorrect, user dies
        if int(guess) != good_pod:
            print(dedent("""
                    You jump into pod {guess} and hit the eject button.
                    The pod escapes out into the void of space, then
                    implodes as the hull ruptures, crushing your body into
                    jam jelly.
                    """))
            return 'death'

        # if guess is correct, user lives
        else:
            print(dedent("""
                    You jump into pod {guess} and hit the eject button.
                    The pod easily slides out into space heading to the
                    planet below.  As it flies to the planet, you look
                    back and see your ship implode then explode like a
                    bright star, taking out the Gothon ship at the same
                    time.  You won!
                    """))
            return 'finished'

        
# finished scene (last scene)
class Finished(Scene):

    # override enter()
    def enter(self):
        # print congratulatory message
        print('You won! Good job.')
        return 'finished'


# Map class, stores the scenes and changes between them
class Map(object):

    # dict of scene names and corresponding class
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        # store the starting scene
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        # return the scene class specified by scene_name
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        # return the opening/first scene class
        return self.next_scene(self.start_scene)


# create Map object and set opening scene to central_corridor
a_map = Map('central_corridor')
# create Engine object with a_map as the scene_map
a_game = Engine(a_map)
# start the game
a_game.play()
