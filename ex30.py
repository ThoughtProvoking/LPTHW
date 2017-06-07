# set people to 30
people = 30
# set cars to 40
cars = 40
# set trucks to 15
trucks = 15

# if cars greater than people, take cars
if cars > people:
    print('We should take the cars.')
# if cars less than people, don't take cars
elif cars < people:
    print('We should not take the cars.')
# else (cars equal people), can't decide
else:
    print("We can't decide")

# if trucks greater than cars, don't take trucks
if trucks > cars:
    print("That's too many trucks.")
# if trucks less than cars, take trucks
elif trucks < cars:
    print('Maybe we should take the trucks.')
# else (trucks equal cars), can't decide
else:
    print("We still can't decide")

# if people greater than trucks, take trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
# else (people less than or equal to trucks), stay home
else:
    print("Fine, let's stay home then.")

# 1.) If the if-statement fails, the code moves onto the elif-statement.
#   If the elif-statement fails, the code moves onto the else-statement.
#   Else-statement will always run if the if and elif are False.
#
# 2.) people = 4512, cars = 8465, trucks = 9864
#   Output:
#       We should take the cars.
#       That's too many trucks.
#       Fine, let's stay home then.
# 3.)
# if people < trucks < cars, print message
if people < trucks and trucks < cars:
    print("People are less than trucks, which is less than cars.")
# if people > trucks > cars, print message
elif people > trucks and trucks > cars:
    print("People are greater than trucks, which is greater than cars.")
# else, print confused message
else:
    print("I'm not sure how many people, trucks and cars there are.")
