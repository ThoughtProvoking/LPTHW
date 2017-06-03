# set number of cars to 100
cars = 100
# set space_in_a_car to 4 (4 or 4.0 does not matter because value is never used in division)
space_in_a_car = 4.0
# set number of drivers to 30
drivers = 30
# set number of passengers to 90
passengers = 90
# calculate number of cars not being driven
cars_not_driven = cars - drivers
# set number of cars driven to number of drivers
cars_driven = drivers
# calculate maximum number of people that can be carpooled
carpool_capacity = cars_driven * space_in_a_car
# calculate average passengers per driven car
average_passengers_per_car = passengers / cars_driven


# print number of cars
print('There are', cars, 'cars available.')
# print number of drivers
print('There are only', drivers, 'drivers available.')
# print number of cars not being driven
print('There will be', cars_not_driven, 'empty cars today.')
# print the maximum number of people that can be carpooled
print('We can transport', carpool_capacity, 'people today.')
# print the number of passengers
print('We have', passengers, 'to carpool today.')
# print average passengers per driven car
print('We need to put about', average_passengers_per_car, 'in each car.')
