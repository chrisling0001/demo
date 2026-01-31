from operator import attrgetter


class Person():
    blood_color = "red"
    skin = "yellow"
    eyes = "Black and White"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello, " + self.name.title() + " you're "
                 + str(self.age) + " years old.")

class User():
    def __init__(self, user_id):
        self.user_id = user_id
    
    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u:u.user_id))

