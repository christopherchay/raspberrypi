import random
import time
import sys

def navigation():

   hp = 5
   ham = 0
   coin = 0
   medicine = 0
   monsterkilled = 0
   roomdiscovered = 0
   
   longtitude = 2
   latitude = 2
   xaxis = 0
   yaxis = 0
   
   x = "x"
   divline = "---------------"
   
   # |a|b|c|
   #----------
   # |d|e|f|
   #----------
   # |g|h|i|
   
   
   def makeMap( x ):
      print( divline )
      print( '| ' + x[ 0 ] + ' | ' + x[ 1 ] + ' | ' + x[ 2 ] + ' |' )
      print( divline )
      print( '| ' + x[ 3 ] + ' | ' + x[ 4 ] + ' | ' + x[ 5 ] + ' |' )
      print( divline )
      print( '| ' + x[ 6 ] + ' | ' + x[ 7 ] + ' | ' + x[ 8 ] + ' |' )
      print( divline )
   
   position = [ '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ' ]
   
   def displayPosition( x, y ):
      x[y] = ('x') 
   
   def recreateMap():
      global position
      position.remove('x')
      position.append('  ')
   
   ## Do not use i,t, m , n or any wide letter or thin letter g , f, included
   
   # pass 1 parameter instead of passing in 9 parameters
   # hint: Need to modify makeBoard and  displayMap function
   
   def displayMap():
      global square, x
      if xaxis == -1 and yaxis == 1:
         displayPosition( position, 0 )
         makeMap( position )
         recreateMap()
   
      elif xaxis == 0 and yaxis == 1:
         displayPosition( position, 1 )
         makeMap( position )
         recreateMap()
   
      elif xaxis == 1 and yaxis == 1:
         displayPosition( position, 2 )
         makeMap( position )
         recreateMap()
   
      elif xaxis == -1 and yaxis == 0:
         displayPosition( position, 3 )
         makeMap( position )
         recreateMap()
   
      elif xaxis == 0 and yaxis == 0:
         displayPosition( position, 4 )
         makeMap( position )
         recreateMap()
   
      elif xaxis == 1 and yaxis == 0:
         displayPosition( position, 5 )
         makeMap( position )
         recreateMap()
   
      elif xaxis == -1 and yaxis == -1:
         displayPosition( position, 6 )
         makeMap( position )
         recreateMap()
   
      elif xaxis == 0 and yaxis == -1:
         displayPosition( position, 7 )
         makeMap( position )
         recreateMap()
         
      elif xaxis == 1 and yaxis == -1:
         displayPosition( position, 8 )
         makeMap( position )
         recreateMap()
   
      else:
         print('WARNING! SOMETHING WRONG!!')
   
   
   ## Startouts for the player. They accumilate overtime.
   def printInventory():
      print('HP:', hp)
      print('Ham:', ham)
      print('Coins:', coin)
      print('Bottles of medicine:', medicine)
   
   def printTotalScore():
      global hp, ham, coin, medicine, roomdiscovered, monsterkilled, name
      ham_score = ham*1
      medicine_score = medicine*2
      coin_score = coin*2
      roomdiscovered_score = roomdiscovered*1
      monsterkilled_score = monsterkilled*3
      total_score = ham_score + medicine_score + coin_score + roomdiscovered_score + monsterkilled_score
      print(name + '\'s total score is', total_score)
   
   def showItemsCollected():
      global ham, medicine, coin
      itemscollected = ham + medicine + coin
      return itemscollected
   
   # This tells you what exactly happens when you movve into a room.
   def displayRandEvent():
      randEvent = random.randint(0,2)
      global hp, ham, coin, medicine, roomdiscovered, monsterkilled
      roomdiscovered = roomdiscovered + 1
      if randEvent == 0:
         print('A monster attacks', name, '!!')
         m = 1
         while m > 0 or hp > 0:
            attack = random.randint(1,10)
            if attack < 6:
               hp = hp - 1
               print('OUCH!', name, 'has been hit by the monster')
               print('HP:',hp)
               time.sleep(0.5)
            elif attack > 5:
               print(name, 'has successfully killed the monster!!')
               monsterkilled = monsterkilled + 1
               break
            if hp == 0:
               print(name, 'died!!!')
               break
      elif randEvent == 1:
         print('The room is empty.')
      elif randEvent == 2:
         item = random.randint(0,3)
         if item == 0:
            prize = ("a gold coin")
            coin = coin + 1
            print(gender + ' found ' + prize)
         elif item == 1:
            prize = ("a bottle of medicine")
            hp = hp + 1
            medicine = medicine + 1
            print(gender + ' found ' + prize)
         elif item == 2:
            prize = ("a leg of ham")
            ham = ham + 1
            print(gender + ' found ' + prize)
   
   def displayAction():
      global direction, name
      print(name, 'walked', direction, '.....')
      displayMap()
      displayRandEvent()
      printInventory()
   
   def showCharacScore():
      print('''######################################
   Character total score:
   ''')
      print('NAME: ' + name + '\n')
      print('Total items collected:', showItemsCollected())
      printInventory()
      print('\nRooms explored:', roomdiscovered)
      print('Monsters killed:', monsterkilled)
      printTotalScore()
   
   name = input('What is your name? ')
   gender = input('What is your gender? (type "m" for male,  "f" for female)')
   if gender == "m":
      gender = "He"
   elif gender == "f":
      gender = "She"
   else:
      print(name, ', I don\'t know what you are.')
      gender = name
   
   input('You will be starting in the center room. Try to survive. Good luck. <press enter to continue>')
   displayMap()
   printInventory()
   
   
   while hp > 0:
      print('========================================')
      a = input('Please choose a cardinal direction. "n","s","e","w" (or type "z" to exit): ')
   
      if a == "z":
         break
   
      if a == "n":
         direction = "north"
         if longtitude == 2 or longtitude == 3 :
            yaxis = yaxis + 1
            longtitude = longtitude - 1
            displayAction()
         else: 
            print('A wall is blocking your path.')
      if a == "s":
         direction = "south"
         if longtitude == 1 or longtitude == 2:
            yaxis = yaxis - 1
            longtitude = longtitude + 1
            displayAction()
         else:
            print('A wall is blocking your path.')
      elif a == "e":
         direction = "east"
         if latitude == 1 or latitude == 2:
            xaxis = xaxis + 1
            latitude = latitude + 1
            displayAction()
         else:
            print('A wall is blocking your path.')
      elif a == "w":
         direction = "west"
         if latitude == 2 or latitude == 3:
            xaxis = xaxis - 1
            latitude = latitude - 1
            displayAction()
         else:
            print('A wall is blocking your path.')
   
   showCharacScore()
   