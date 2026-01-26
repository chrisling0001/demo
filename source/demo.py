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