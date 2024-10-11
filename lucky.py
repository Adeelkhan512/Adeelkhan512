import random
team = [ 1,2,3,4]

first = random.randint(0,3)
x = team.pop(first)

print('Lucky draw winner',x)

second = random.randint(0,2)
y = team.pop (second)

print ("lucky draw winner",y)


