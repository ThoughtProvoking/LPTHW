# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'{abbrev} has the city {city}')

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')
    print(f'and has city {cities[abbrev]}')

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print('Sorry, no Texas')

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

# stuff to do with dict-type
#   len(dict)           - return number of items in dict
#   dict[key]           - return item of dict with key 'key'
#   dict[key] = value   - set dict[key] to value
#   del dict[key]       - remove dict[key] from dict
#   key in dict         - True if dict has key 'key'
#   key not in dict     - True if dict has no key 'key'
#   iter(dict)          - returns iterator over the keys of dict
#   clear()             - removes all items in dict
#   copy()              - returns shallow copy of dict
#   fromkeys(seq)       - creates new dict with keys from seq and sets values to None
#   get(key)            - returns value for key if exists
#   items()             - returns items of dict in (key, value) pairs
#   keys()              - returns keys of dict
#   pop(key)            - remove and return value of key
#   popitem()           - remove and return random (key, value) pair of dict
#   setdefault(key)     - return key's value if exists, else insert key with value None
#   update([other])     - overwrite existing keys with values from other
#   values()            - returns values of dict
