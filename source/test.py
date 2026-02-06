from collections import defaultdict, Counter, deque, namedtuple
from enum import Enum
""" def a_new_decorator(a_func):
    def wrap_the_function():
        print("I'm doing some boring work b4 executing a_func()")
        a_func()
        print("I'm doing some boring work after executing a_func()")
    return wrap_the_function

def a_function_requring_decoration():
    print("I'm the function which needs some decoration" \
            " to remove my foul smell.")

@a_new_decorator
def a_function_requring_decoration():
    # Hey you! Decorate me!
    print("I'm the function which needs some decoration" \
            " to remove my foul smell") """

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9

    kitten = 1 
    puppy = 2 

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=22, type=Species.cat)
dragon = Animal(name='dragon', age=92, type=Species.dragon)
print(perry)
print(dragon)