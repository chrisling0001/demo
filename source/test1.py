from datetime import timedelta, datetime, date
import calendar, pytz, itertools, io, os

filename = 'source/test.txt'

def date_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def __repr__(self):
        return 'Node({!r})'.format(self.value)
    
    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)
    
    def depth_first(self):
        yield self
    
def frange(start, stop, increment=0.5):
    x = start
    while x < stop:
        yield x
        x += increment

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

