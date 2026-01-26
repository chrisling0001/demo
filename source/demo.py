class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("Hello, " + self.name.title() + " you're "
                 + str(self.age) + " years old.")
        
me = Person("chrisling", 21)
you = Person("ayaka", 22)
me.greet()
you.greet()