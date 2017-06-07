people = 34
cats = 45
dogs = 65

if people < cats:
    print('Too many cats! The world is doomed!')

if people > cats:
    print('Not many cats! The world is saved!')

if people < dogs:
    print('The world is drooled on!')

if people > dogs:
    print('The world is dry!')

dogs += 5

if people >= dogs:
    print('People are greater than or equal to dogs.')

if people <= dogs:
    print('People are less than or equal to dogs.')

if people == dogs:
    print('People are dogs.')

# 1.) if the condition following the 'if' keyword is evaluated to True,
#   the code underneath is executed. Otherwise, the code is skipped over.
#
# 2.) Code under the 'if' keyword needs to be indented so python knows what
#   code to execute if the condition passes and what code to run regardless
#   of the condition.
#
# 3.) If the code is not indented, it will be run regardless of the if-condition.
#
# 4.) 
if (3 == 3) and (not ("testing" == "testing" or "Python" == "Fun")): # False
    print("This won't run.")

if (1 == 1) and (not ("testing" == 1 or 1 == 0)): # True
    print("This will run.")
#
# 5.) If you change the initial values for people, cats, and dogs, the conditions
#   in the if-statements may change, so the code that is ran (and consequently the output)
#   may be different.
