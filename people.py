# get people
# Hugh Smith

# imports
import json

# classes
class Person:
    def __init__(self, gender, title, first, last, street, city, state,
     postcode, latitude, longitude, offset, description, email, uuid, 
     username, password, salt, md5, sha1, sha256, date, age,
     date_registered, age_registered, phone, cell, picture, nat):
        self.gender = gender
        self.title = title
        self.first = first
        self.last = last
        self.street = street
        self.city = city
        self.state = state
        self.postcode = postcode
        self.latitude = latitude
        self.longitude = longitude
        self.offset = offset
        self.description = description
        self.email = email 
        self.uuid = uuid
        self.username = username
        self.password = password
        self.salt = salt
        self.md5 = md5
        self.sha1 = sha1
        self.sha256 = sha256
        self.date = date
        self.age = age
        self.date_registered = date_registered
        self.age_registered = age_registered
        self.phone = phone
        self.cell = cell
        self.picture = picture
        self.nat = nat

    # methods
    
    # return the name
    def get_name(self):
        return self.title+" "+self.first+" "+self.last

    # return the location
    def get_location(self):
        return (self.latitude, self.longitude)


# functions

# get and return some ammount of people
def get_people(ammount = 5000): # defult value of 5000
    '''
    @param : int
    @returns list
    @throws : valueError
    '''
    # check if the inputed value is over 5000 the max
    if ammount > 5000:
        ammount = 5000
    
    # get the data from the text file in json formating
    with open("people_txt.txt") as data_txt:
        data = json.load(data_txt)
        data = data["results"]
    
    # the data base
    people_db = []

    # add the people into the data base
    for person in data:
        gender = person["gender"]
        title = person["name"]["title"]
        first = person["name"]["first"]
        last = person["name"]["last"]
        street = person["location"]["street"]
        city = person["location"]["city"]
        state = person["location"]["state"]
        postcode = person["location"]["postcode"]
        latitude = person["location"]["coordinates"]["latitude"]
        longitude = person["location"]["coordinates"]["longitude"]
        offset = person["location"]["timezone"]["offset"]
        description = person["location"]["timezone"]["description"]
        email = person["email"]
        uuid = person["login"]["uuid"]
        username = person["login"]["username"]
        password = person["login"]["password"]
        salt = person["login"]["salt"]
        md5 = person["login"]["md5"]
        sha1 = person["login"]["sha1"]
        sha256 = person["login"]["sha256"]
        date = person["dob"]["date"]
        age = person["dob"]["age"]
        date_registered = person["registered"]["date"]
        age_registered = person["registered"]["age"]
        phone = person["phone"]
        cell = person["cell"]
        picture = person["picture"]["large"]
        nat = person["nat"]


        people_db.append(Person(gender, title, first, last, street, city, state,
     postcode, latitude, longitude, offset, description, email, uuid, 
     username, password, salt, md5, sha1, sha256, date, age,
     date_registered, age_registered, phone, cell, picture, nat))

    # return the data base
    return people_db





# main routine

# testing
if __name__ == "__main__":
    people_db = get_people(5000)
    print(people_db[600].get_name())    