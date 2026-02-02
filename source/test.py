import re, os, re
import unicodedata
from urllib.request import urlopen
from fnmatch import fnmatch, fnmatchcase

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFC', s2)

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
# print(t3 == t4)
print(''.join(c for c in t1 if not unicodedata.combining(c)))