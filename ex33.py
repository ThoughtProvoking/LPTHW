# 1.) Convert code into a function with one argument (n: number of elements in list)
# 2.) Add second argument (m: how much to increment each element)
def create_list(n, m):
    # set i to 0
    i = 0
    # set numbers to empty list
    numbers = []

    # while i less than n
    while i < n:
        print(f'At the top i is {i}')
        # append element i
        numbers.append(i)

        # increment i by m
        i += m
        print('Numbers now: ', numbers)
        print(f'At the bottom i is {i}')

    print('The numbers: ')

    # print every element
    for num in numbers:
        print(num)


# 5.) Rewrite function to use for-loop and range()
def create_list_for(n, m):
    # set numbers to empty list
    numbers = []

    # loop through 0 to n, incrementing by m AFTER every iteration
    for i in range(0, n, m):
        print(f'At the top i is: {i}')
        # append element i
        numbers.append(i)

        # if incrementor is not removed, 
        # element will increase twice every loop
        print('Numbers now: ', numbers)
        print(f'At the bottom is is {i}')

    print('The numbers: ')

    # print every element
    for num in numbers:
        print(num)


#create_list(3)
create_list(20, 3)
create_list_for(20, 3)
