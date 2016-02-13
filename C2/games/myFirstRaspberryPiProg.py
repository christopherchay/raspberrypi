import random
import time
import sys

print("This a knight game where you battle monsters and climb the ladder to success.")

health = 10
medicine = 0
bottlesOfMedicine = []
pack = [ "dagger" ]
gold = 25
level = 1
expirence = 0
damage = random.randint( 1, 3 )
damage2 = random.randint( 1, 2 )


def hit():
    hit = [ "lacerated", "cut", "stabbed", "swung" ]
    return hit [ random.randint( 0, 3 ) ]

def knapsack():
    print()
    print( 'Knapsack:' )
    print( "Health: ", health )
    print( "gold: ", gold )
    print( "level: ", level )
    print( "Items in pack:", pack )
    print( "Expirence:", expirence )
    print()

def shop():
    global health, gold
    print("The healer will heal you if you need it. ")
    action = input("''s(leep)'  or \"e\" to exit. ")
                
    if action.startswith( 's' ) and level == 1 and health < 3 :
        health += 10
        gold -= 10
        print()
    elif action== "e":
        pass

def randAnimal():
    animal = [ "Wolf","Snake","Monkey","Racoon" ]
    return animal[ random.randint( 0, 3 ) ]




def mountain():
    global expirence
    print( 'A changing monster roams the mountains, so be careful.' )
    input( '<Press enter to continue>' )
    print( 'Would you like to fight the', randAnimal(), '? (f)ight or (r) unaway' )
    action = input()
    if action.startswith( 'f' ):
        global health
        hp2 = random.randint( 5, 10 )
        while health > 2 and hp2 > 0:
            acoh = random.randint( 0, 1 )
            dcoh = random.randint( 0,1 )

            if acoh == 0:
                print( randAnimal(), 'missed it\'s strike.'  )
            else:
                print( randAnimal(), 'has bit you for', damage2, 'damage.' )
                health -= damage2
            if dcoh == 0:
                print( 'You missed!!' )
                print( '{}, Health: {}' .format( name, health ) )
                print( '{}, Health: {}' .format( randAnimal(), hp2 ) )
            else:
                print( 'You', hit(), 'at the', randAnimal(), 'for', damage, 'damage.' )
                hp2 -= damage
                print( '{}, Health: {}' .format( name, health ) )
                print( '{}, Health: {}' .format( randAnimal(), hp2 ) )
                print( '=====================================' )
    elif action.startswith( 'r' ):
        print( 'You run away.' )

    if health < 2:
        print( 'You have been hurt very badly. Go and heal yourself quickly.' )
        expirence += 10
    elif health == 0:
        print( 'Oh no!! You died!!' )
    elif hp2 <= 0:
        print( 'You have defeated the', randAnimal() )
        expirence += 10        

def forge():
    global gold, pack, damage
    while True:
        action = input( """Blacksmith: Hey ther' chap. Can I help yer with anything?
'b'(uy) or 'w'(ork)
""" )
        if action == "b":
                action = input( """Blacksmith: Don't got much to show.
's'(word) cost: 100g, 'a'(xe) cost: 300g, 'flail' cost: 500g
""" )
                if action.startswith( 's' ) and gold > 99:
                    gold  -= 100
                    print( 'You bought the sword.' )
                    pack.append( "sword" )
                    damage = random.randint( 4, 6 )
                elif action.startswith( 'a' ) and gold > 299:
                    gold  -= 300
                    print( 'You bought the axe.' )
                    pack.append( "axe" )
                    damage = random.randint( 7, 9 )
                elif action.startswith( 'f' ) and gold > 499:
                    gold  -= 500
                    print( 'You bought the flail.' )
                    pack.append( "flail" )
                    damage = random.randint( 10, 12 )
                else:
                    continue
                                           
        elif action == "w":
            input( '' )
        elif action == "z":
            break
        else:
             print( "Something went wrong." )

name = input( "Welcome, brave one. What is your name? " )
print(name, """, you have been sent to train in the city of Arna.
You can fight, buy, and do virtually anything the game allows.
""" )
action = input( "Type 'i' to view your inventory. " )
if action == "i":
    knapsack()

print("""You can visit the 'forge' to get new armours and weapons,
You can go to the 'inn' to regain your health.
Or you can go to the 'forest' to fight monsters.
""")
while health > 0:
    action = input("You can type 'shop', 'mt'(mountain),'fe(forge)' , or 'i'(nventory) or \"z\" to exit.  ")
    if action.startswith( 's' ):
        print("You went to the shop.")
        shop()
    elif action.startswith( 'm' ):
        print("You went to the mountains.")
        mountain()
    elif action.startswith( 'f' ):
        print("You went to to the forge.")
        forge()
    elif action.startswith( 'i' ):
        knapsack()

    if action == "z":
        sys.exit()
   
    if expirence == 50:
        level += 1
        gold += 50
        print( 'Congratulations!! You have acheived level 2!!' )
    



