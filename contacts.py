# Libraries

from replit import db

import time
from time import sleep

#

# Classes

class Contacts:
  def __init__(self, key):
    self.uKey = key
    self.cons = db[key]
    pass

  def addCon(self, conName, conNum):
    newCon = [
      conName,
      conNum
    ]

    self.cons.append(newCon)

    selected_con = len(self.cons.value[0])
    print(selected_con)

    print(self.cons.value[0])
    return

#

# Functions

def init():
  name = input('Enter your set name \n(If you don\'t have one, then type in \'create new name\'): ')

  if name == 'create new name':
    print('===')
    newName = input('What name would you like to set? \n(you will use this name to view your saved contacts): ')
    print('Checking Availability...')
    
    canChoose = checkDB(newName)

    if canChoose:
      print('Name is available!')
      db[newName] = []
      print('Getting things ready...')
      setUpCon(True, newName)

  else:
    addSpace()
    

def setUpCon(isNew: bool, key: str):
  cons = Contacts(key)
  
  if isNew:
    print('===')
    print('Let\'s set up your first contact...')

    con_name = input('Enter a name for your contact: ')

    if con_name != '':
      con_num = input('Enter a phone number for your contact \n(This doesn\'t have to be a real phone number): ')

      if con_num != '':
        print('Setting up contact...')
        sleep(0.5)
        addSpace()
        cons.addCon(con_name, con_num)
        
        
    
def checkDB(key):
  keys = db.keys()

  for k in keys:
    if key == k:
      return False

  return True

def addSpace():
  print('\n')
  print('===')
  print('\n')
  
#

init()