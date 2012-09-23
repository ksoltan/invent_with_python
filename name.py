# This gives you a new name

import random
import time

print('Hello, what is your name?')#This is where everything begins.
myName = input()
print('Hi, '+myName+'. Would you like a new name?')
want_new_name = input() == 'yes'

def newName(myName, newName):
    print('Well, '+myName+', your new name is '+newName+'.')
    time.sleep(1)
    print('Hello '+newName+'. Do you like your new name?')
    return input() != 'yes'
        
while want_new_name:
    name = random.randint(1, 4)
    y = "Unknown"
    if name == 1:
        y = "Geb"
    if name == 2:
        y = "Shu"
    if name == 3:
        y = "Ra"
    if name == 4:
        y = "Bast"
    want_new_name = newName(myName, y)


        
    

    
