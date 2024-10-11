# create a dict


country = {
    'Pakistan':'Lahore',
    'England':'Karachi',
    'UAE':'Abu Dhabi',
    'ID':123
}


print('Countries Detail :',country)


# immutable
# keys must be immutable

# Access
print('country capital:',country['England'])



# Add item 
country['Italy'] = 'Rome'
print(country)



# remove ditionary

del country['England']
print(country)

# clear method
#country.clear()
#print(country)



# change item in dict

country['Italy'] = 'Istanbul'
print(country)


# dict for loop

for coun in country:
    print(coun)


# dict wit for loop in print value


'''for coun in country:
    capital = country[coun]
    print(capital)

 '''

