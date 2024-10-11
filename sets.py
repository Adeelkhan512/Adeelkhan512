# Create a new set

std_id = {2,22,24,44,55,12}
print("Student Id:", std_id)


# Mix data

std = {'umer',2,'Ali',22,'Adeel',44}
print('student data:',std)



# empty set




# create a empty set
empty = {}
print('Data types',type('empty_set'))

#Check data type
print('data type with data',type(empty))


# duplicate
numbers = {2,2,3,3,4,5,6,7,8,980,89,}
print(numbers)



# add item in python 
print('initial Numbers:',numbers)


numbers.add(89)
print('updated set:',numbers)

# remove 
remove_value = numbers.discard(89)
print('after remove value:',numbers)


# union of two sets
# first set
 
A = {1,2,3}
# second set


B ={ 2,4,0}
print('union string:',A|B)


print( 'using union method:',A.union (B))




