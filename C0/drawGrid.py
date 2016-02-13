# generates grids
# todo: make it work with even numbered gridSize

# init
gridSize= 5
playerX = 0
playerY = 0
playerGridLoc={"x":playerX, "y":playerY} #works with even locations

monsterX = 4
monsterY =4
monsterGridLoc={"x":monsterX, "y":monsterY} #works with even locations

# setup
y=gridSize * 2 +1
x=gridSize * 2 +1
playerCalculatedLoc={"x":playerGridLoc["x"]+2, "y":playerGridLoc["x"]+2}
monsterCalculatedLoc={"x":monsterGridLoc["x"]+2, "y":monsterGridLoc["x"]+2}


#, end=""
def drawHor( yi ):
   if ( yi == y ): #end of line
      print( "-" )
   else:
      print( "-", end="" )
      
def drawVert( xi ):
   if ( xi == x ): #end
      print( "|" )
   else: #others
      print( "|", end=""  )

def drawCell( playerCalculatedLoc, monsterCalculatedLoc, xi, yi ):
   if ( playerCalculatedLoc["x"] == xi and playerCalculatedLoc["y"] == yi ):
      print( "p", end="")
   elif ( monsterCalculatedLoc["x"] == xi and monsterCalculatedLoc["y"] == yi ):
      print( "m", end="")
   elif ( ( playerCalculatedLoc["x"] == xi and playerCalculatedLoc["y"] == yi ) and ( monsterCalculatedLoc["x"] == xi and monsterCalculatedLoc["y"] == yi  )):
      print( "x", end="")
   else:
      print( "  ", end="")
   
for yi in range( 1, y+1 ): # each row = y
   for xi in range( 1, x+1 ): # each column =x
      if ( ( yi % 2 ) != 0  ): # Odd row only "-"
         drawHor( xi )
      else : # even row only "- |"
         if ( ( xi % 2 ) != 0 ): # Odd vert only "|"
            drawVert( xi )
         elif ( ( xi % 2 ) == 0 ): # Even Vert
            drawCell( playerCalculatedLoc, monsterCalculatedLoc, xi, yi)
         elif ( xi ==x ): # last
            drawHor( yi)

def moveMonster( directionX, directionY ):
   global monsterX, monsterY, playerCalculatedLoc, monsterCalculatedLoc, xi, yi
   monsterX = monsterX +directionX
   monsterY = monsterY +directionY
   drawCell( playerCalculatedLoc, monsterCalculatedLoc, xi, yi )

