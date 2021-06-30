import os
import random

a = 'yes you are dumb'
b = 'no you are smart'
list = [a, b]
c = random.choice(list)
print(c)
a = input('press any key to go back to the programs page')
if a == "":
    os.startfile('programs.py')
