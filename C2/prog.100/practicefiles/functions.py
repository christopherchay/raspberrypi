def printStatus():
   print( status )
def create():
   global workers, lumbermen, foragers, foodPerTurn, woodPerTurn, food
   create = input( 'What would you like to create? \
"l", "w", "f"? ' )
   if create == "f" and workers > 0:
      foragers += 1
      workers -= 1
      foodPerTurn += 1
   elif create == "l" and workers > 0:
      lumbermen += 1
      woodPerTurn += 1
      workers -= 1
   elif create == "w" and food > 3:
      workers += 1
      food -= 3

def destroy():
   global workers, lumbermen, foragers
   create = input( 'What would you like to destroy? \
"l", "w", "f"? ' )
   if destroy == "f":
      foragers -= 1
   elif destroy == "l":
      lumbermen -= 1
   elif destroy == "w":
      worker -= 1


foodPerTurn = 0
woodPerTurn = 0

food = 0
wood = 0

workers = 3
lumbermen = 0
foragers = 0


while True:
   food = foodPerTurn + food
   wood = woodPerTurn + wood
   print()
   print( 'Worker Status:', 'W:', workers, 'F:', foragers, 'L:', lumbermen )
   print()
   print( 'Food:', food, 'Wood:', wood )
   action = input( 'Manage your workers: "c" or "d" ' )

   if action == "c":
      create()
   elif action == "d":
      destroy()

   if wood >= 50 and food >= 50:
      break

if wood >= 50 and food >= 50:
   print( 'You win' )
   
      
      
