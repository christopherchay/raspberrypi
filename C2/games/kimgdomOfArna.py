## We will define the profile, and we can go on to dungeons.

import random
import sys

print( 'Welcome to the Kingdom of Arna.' )

players = []
player = 0
maxPlayers = 3

while len( players ) < maxPlayers:
	player += 1
	profile = { 'life': 20, 'name': "", 'race': "", 'exp': 0, 'gold': 0, 'weapon': "", 'damage': 0, 'inventory': [] }

	name = input( 'What is thy name? ' )
	race = input( 'What is thy race? ( borderlander / woodlander / knight )' )
	if race.startswith( 'b' ):
		profile[ 'race' ] = "Borderlander"
		profile[ 'weapon' ] = "axe"
		profile[ 'damage' ] = random.randint( 1,7 )
	elif race.startswith( 'k' ):
		profile[ 'race' ] = "Knight"
		profile[ 'weapon' ] = "sword"
		profile[ 'damage' ] = random.randint( 1,5 )
	elif race.startswith( 'w' ):
		profile[ 'race' ] = "Woodlander"
		profile[ 'weapon' ] = "bow"
		profile[ 'damage' ] = random.randint( 1,6 )
		profile[ 'ammo' ] = 50
	
	profile[ 'name' ] = name
	
	players.append( profile )
	

	if player == 3:
		break

print( players[0] )
print( players[1] )
print( players[2] )

ammo = players[1][ 'ammo' ]

guy1 = players[0][ 'name' ]
guy2 = players[1][ 'name' ]
guy3 = players[2][ 'name' ]

hp1 = players[0][ 'life' ]
hp2 = players[1][ 'life' ]
hp3 = players[2][ 'life' ]

w1 = players[0][ 'weapon' ]
w2 = players[1][ 'weapon' ]
w3 = players[2][ 'weapon' ]

dd1 = players[0][ 'damage' ]
dd2 = players[1][ 'damage' ]
dd3 = players[2][ 'damage' ]


print( 'this is the first dungeon.' )
print( 'The Kelleri pub.' )
bguy1 = 'Bartender'
bguy2 = 'guest'
bguy3 = 'lumberjack'
ehp1 = random.randint( 5, 15 )
ehp2 = random.randint( 5, 15 ) 
ehp3 = random.randint( 5, 15 )
print( guy1, hp1, w1 )
print( guy2, hp2, w2 )
print( guy3, hp3, w3 )
print( bguy1, ehp1 )
print( bguy2, ehp2 )
print( bguy3, ehp3 )
input()
while hp1 > 0 or hp2 > 0 or hp3 > 0:

	if hp1 <= 0 and hp2 <= 0 and hp3 <= 0 or ehp1 <= 0 and ehp2 <= 0 and ehp3 <= 0: 
		break

	ed1 = random.randint( 1, 5 ) 
	ed2 = random.randint( 1, 5 ) 
	ed3 = random.randint( 1, 5 )
	edd1 = random.randint( 1, 5 )
	edd2 = random.randint( 1, 5 ) 
	edd3 = random.randint( 1,5 )
	d1 = random.randint( 1, 5 ) 
	d2 = random.randint( 1, 5 ) 
	d3 = random.randint( 1, 5 )
	
	if ed1 > 3:
		if d1 > 3:
			print( guy1, 'dodged the attack.' )
		else:
			hp1 -= edd1
			print( bguy1, 'hit', guy1, 'for', edd1 )
	else:
		print( bguy1, 'missed' )
	 
	if ed2 > 3:
		if d2 > 3:
			print( guy2, 'dodged the attack.' )
		else:
			hp2 -= edd2
			print( bguy2, 'hit', guy2, 'for', edd2 )
	else:
		print( bguy2, 'missed' )
	 
	if ed3 > 3:
		if d3 > 3:
			print( guy3, 'dodged the attack.' )
		else:
			hp3 -= edd3
			print( bguy3, 'hit', guy3, 'for', edd3 )
	else:
		print( bguy3, 'missed' )
	 
	 
	 
	 
	 
	 
	 
	 
	 
	if dd1 > 3:
		if ed1 > 3:
			print( bguy1, 'dodged the attack.' )
		else:
			ehp1 -= dd1
			print( guy1, 'hit', bguy1, 'for', dd1 )
	else:
		print( guy1, 'missed' )
	
	if edd2 > 3:
		if ed2 > 3:
			print( bguy2, 'dodged the attack.' )
		else:
			ehp2 -= dd2
			print( guy2, 'hit', bguy2, 'for', dd2 )
	else:
		print( guy2, 'missed' )
	
	if edd3 > 3:
		if ed3 > 3:
			print( bguy3, 'dodged the attack.' )
			ammo -= 1
		else:
			ehp3 -= dd3
			print( guy3, 'hit', bguy3, 'for', dd3 )
			ammo -= 1
	else:
		print( guy3, 'missed' )
		ammo -= 1
	 
	print()
	print( guy1, hp1, w1 )
	print( guy2, hp2, w2 )
	print( guy3, hp3, w3 )
	print( bguy1, ehp1 )
	print( bguy2, ehp2 )
	print( bguy3, ehp3 )
	print()


sys.exit()







