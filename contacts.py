# Libraries

from replit import db

import time
from time import sleep

#

# Classes

class Contacts:
  def __init__(self, key: str):
    self.uKey = key
    self.cons = db[key]
    pass

  def addCon(self, conName: str, conNum: str):
    newCon = [
      conName,
      conNum
    ]

    self.cons.append(newCon)
    addSpace()
    
    return

  def getCons(self):
    return self.cons.value

#

# Functions

def init():
  name = input('Enter your set name \n(If you don\'t have one, then type in \'create new name\'): ')

  if name == 'create new name':
    print('===')
    newName = input('What name would you like to set? \n(you will use this name to view your saved contacts): ')
    print('Checking Availability...')
    
    chosenName = checkDB(newName)

    if not chosenName:
      print('Name is available!')
      db[newName] = []
      print('Getting things ready...')
      setUpCon(True, newName)
  
  else:
    addSpace()

    keyExi = checkDB(name)

    if keyExi:
      setUpCon(False, name)
    else:
      print('This name doesn\'t exist!')
      sleep(1)
      addSpace()
      init()
    

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

        loadCons(key)

  else:
    loadCons(key)

def loadCons(key: str):
  consClass = Contacts(key)
  cons = consClass.getCons()

  for c in cons:
    print(c[0])
    print(c[1])
    print('\n')

  print('Type \'log out\' to go back to the main screen')
  conToAdd_name = input('Contact Name: ')

  if conToAdd_name != '' and conToAdd_name != 'log out':
    conToAdd_num = input('Contact Number: ')

    if conToAdd_num != '':
      consClass.addCon(conToAdd_name, conToAdd_num)

      loadCons(key)

  if conToAdd_name == 'log out':
    addSpace()
    init()
    
def checkDB(key):
  keys = db.keys()

  for k in keys:
    if key == k:
      return True

  return False

def addSpace():
  print('\n')
  print('===')
  print('\n')
  
#

init()