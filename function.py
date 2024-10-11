'''def greet():
    print('hellow python class')

greet()

def greet():
    print('hello :','name')
greet('Adeel')


'''





def find_square(num):
    result = num * num
    return result


# function call
square = find_square(9)
print("square is :",square)

# function with arbitary Arguments, *args


def find_sums(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    
    print("sum is :" , result)

find_sums(1,2,3,5,7)


def find_sub(*numbers):
    result = 0

    for num in numbers:
        result = result - num


    print("sub is :"  , result)

find_sub(12-28)


# decalre globally variable

message = 'Hello Python'

def names():
    print('Local',message)

names()

print("Globally :", message)


    









