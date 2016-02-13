import random, time

print('''WARRIOR\'S QUEST!
All done in python!
Presented by Peter Mopark!''')

gold = 100
hp = 10
level = 1
   
longtitude = 2
latitude = 2
xaxis = 0
yaxis = 0

square = "|  "
x = "|x"
m = "|m"
i = "|i"
a = "|a"
g = "|g"
t = "|t"
w = "|w"
divline = "---------"

def enterArmoury():
   pass
def enterWeaponry():
   pass
def enterInn():
   pass
def enterMouintain():
   pass
def enterGuild():
   pass
def entertriningCenter():
   pass

# |a|b|c|
#----------
# |d|e|f|
#----------
# |g|h|i|

def makeBoard( a, b, c, d, e, f, g, h, i ):
   print('''Directory
x = you
m = mountains
i = inn
a = armoury
g = guild
t = training center
w = weaponry
''')
   print( divline )
   print( a + b + c + '|' )
   print( divline )
   print( d + e + f + '|' )
   print( divline )
   print( g + h + i + '|' )
   print( divline )

# pass 1 parameter instead of passing in 9 parameters
# hint: Need to modify makeBoard and  displayMap function

def displayMap():
   global square, x
   if xaxis == -1 and yaxis == 1:
      makeBoard( x, square, i, w, square, t, g, square, a )
      y = input('Would you like to go to the mountains?')
      print('You are in the mountains.')
      enterMountain()
   elif xaxis == 0 and yaxis == 1:
      makeBoard( m, x, i, w, square, t, g, square, a )
   elif xaxis == 1 and yaxis == 1:
      makeBoard( m, square, x, w, square, t, g, square, a )
      print('You are at the inn.')
      enterInn()
   elif xaxis == -1 and yaxis == 0:
      makeBoard( m, square, i, x, square, t, g, square, a )
      print('You are at the weaponry.')
      enterWeaponry()
   elif xaxis == 0 and yaxis == 0:
      makeBoard( m, square, i, w, x, t, g, square, a )
   elif xaxis == 1 and yaxis == 0:
      makeBoard( m, square, i, w, square, x, g, square, a )
      print('You are at the training center.')
      enterTrainingCenter()
   elif xaxis == -1 and yaxis == -1:
      makeBoard( m, square, i, w, square, t, x, square, a )
      print('You are at the guild.')
      enterGuild()
   elif xaxis == 0 and yaxis == -1:
      makeBoard( m, square, i, w, square, t, g, x, a )
   elif xaxis == 1 and yaxis == -1:
      makeBoard( m, square, i, w, square, t, g, square, x )
      print('You are at the armoury.')
      enterArmoury()
   else:
      print('WARNING! SOMETHING WRONG!!')


def showInventory():
   global gold, name
   print('HP:', hp)
   print('GOLD:', gold)


def displayAction():
   global direction, name
   print(name, 'walked', direction, '.....')
   displayMap()
   showInventory()

name = input('Please enter your name: ')

print(name + ', you have been sent to train in the town of Arna....')
time.sleep(1)
print('So you travel to the country of Drama...')
time.sleep(1)
print('And to the gates of the strange town...')
time.sleep(1)
print('Mordaunt: Welcome to the town of Arna, ' + name + '. Yes, someone told me of your arrival. The first for you to do is to get out of those nasty clothes and get some new ones.')

show_inventory = input('Type "i" to view your inventory, or press enter to continue.')
if show_inventory == "i":
   showInventory()

print('You and Mordaunt enter the town of Arna...')
time.sleep(1)
while level < 10:
   print('========================================')
   a = input('Please choose a cardinal direction. "n","s","e","w" (or type "z" to exit): ')

   if a == "z":
      break

   if a == "n":
      direction = "north"
      if longtitude == 2 or longtitude == 3 :
         yaxis = yaxis + 1
         longtitude = longtitude - 1
         displayMap()
      else: 
         print('You can not go there.')
   if a == "s":
      direction = "south"
      if longtitude == 1 or longtitude == 2:
         yaxis = yaxis - 1
         longtitude = longtitude + 1
         displayMap()
      else:
         print('You can not go there.')
   elif a == "e":
      direction = "east"
      if latitude == 1 or latitude == 2:
         xaxis = xaxis + 1
         latitude = latitude + 1
         displayMap()
      else:
         print('You can not go there.')
   elif a == "w":
      direction = "west"
      if latitude == 2 or latitude == 3:
         xaxis = xaxis - 1
         latitude = latitude - 1
         displayMap()
      else:
         print('You can not go there.')



