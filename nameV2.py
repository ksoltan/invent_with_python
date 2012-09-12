# This gives you a new name

import random
import time

def intro(myName):
    print('Hi, '+myName+'. Would you like a new name?')
    new=input()
print('Hello, what is your name?')#This is where everything begins.
myName=input()
intro(myName)

def newName(name):
    print('Well, '+myName+', your new name is '+name+'.')
    time.sleep(1)
    print('Hello '+name+'. Do you like your new name?')
    likeName=input()
        
new='yes'            
if new=='yes':  
    name=random.randint(1, 4)
    if name==1:
        name="Geb"
    if name==2:
        name=="Shu"
    if name==3:
        name="Ra"
    if name==4:
        name="Bast"
    newName(name)
likeName='no'
if likeName=='no':
    intro(myName)
    newName(name)
        
    

    
