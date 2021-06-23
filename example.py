# example file
# Hugh Smith

# imports

import people

people_db = people.get_people(30) # can have up to 5000

# atributes
'''
these are refrenced like this

people_db[index].atribute

example:
people_db[0].first

this will get the first name of the person at the first position in the list

atributes:

gender, 
title, 
first, 
last, 
street, 
city, 
state,
postcode, 
latitude, 
longitude, 
offset, 
description, 
email, 
uuid, 
username, 
password, 
salt, 
md5, 
sha1, 
sha256, 
date, 
age,
date_registered, 
age_registered, 
phone, 
cell, 
picture, 
nat
'''


# specific methods
print(people_db[0].get_name())# return the name of the person
print(people_db[0].get_location()) # this will return the location