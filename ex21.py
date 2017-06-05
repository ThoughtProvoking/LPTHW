def add(a, b):
    # print purpose of function
    print(f'ADDING {a} + {b}')
    # return sum of a, b
    return a + b

def subtract(a, b):
    # print purpose of function
    print(f'SUBTRACTING {a} - {b}')
    # return difference of a, b
    return a - b

def multiply(a, b):
    # print purpose of function
    print(f'MULTIPLYING {a} * {b}')
    # return product of a, b
    return a * b

def divide(a, b):
    # print purpose of function
    print(f'DIVIDING {a} / {b}')
    # return quotient of a, b
    return a / b


# print a string
print("Let's do math with just functions!")

# call add() and store into variable
age = add(30, 5)
# call subtract() and store into variable
height = subtract(78, 4)
# call multiply and store into variable
weight = multiply(90, 2)
# call divide() and store into variable
iq = divide(100, 2)

# print results
print(f'Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}')

# A puzzle for extra credit, type it in anyway.
# print a string
print('Here is a puzzle.')

# call functions within functions
#          35 +          74 -             180 *          50 / 2 = -4391
#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#          50 +         180 -            74 *           35 / 2.0 = -1065
what = add(iq, subtract(weight, multiply(height, divide(age, 2.0))))

# print result
print('That becomes: ', what, 'Can you do it by hand?')

# print result of custom formula
print('89 + 23 * ((143 / 18) - 3):', add(89, multiply(23, subtract(divide(143, 18), 3))))
