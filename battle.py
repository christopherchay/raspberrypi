import random
import time


class Player:
    def __init__( self, name ):
        self.name = name
        self.hp = random.randint( 1,50 )
        #self.gold = gold

    def getHurt( self, damage ):
        self.hp = self.hp - damage

    def showName( self ):
        print ( self.name )

    def showHP( self ):
        print ( self.hp )



def resolveBattle( player1, player2 ):
    hit1 = random.randint( 1,100 )
    if hit1 > 60:
        damage2 = random.randint( 1,10 )
        player2.getHurt ( damage2 )
        print ( "Wham!!!!!!!")
        print ( player1.name , " hit " , player2.name, "for", damage2 , " points." )
        print ( player1.name, ": ", player1.hp )
    else:
        print ( player1.name , " missed." )
        print ( player1.name, ": ", player1.hp )

    hit2 = random.randint( 1,100 )
    if hit2 > 60:
        damage1 = random.randint( 1,10 )
        player1.getHurt ( damage1 )
        print ( "Wham!!!!!!!")
        print ( player2.name , " hit " , player1.name, "for", damage1 , " points." )
        print ( player2.name, ": ", player2.hp )
    else:
        print ( player2.name , " missed." ) 
        print ( player2.name, ": ", player2.hp )
    print ( "-----------------------------------------------------")
    time.sleep(1)


def fight ( ):
    while p1.hp > 0 and p2.hp > 0:
        resolveBattle( p1, p2 )
    else:
        if p1.hp <= 0 and p2.hp <= 0 :
            print ( p1.name, " just died")
            print ( p2.name, " just died" )
        elif p1.hp < 0:
            print ( p1.name, "just died")
            print ( p2.name, ": ", p2.hp )
        else:
            print ( p2.name, "just died")
            print ( p1.name, ": ", p1.hp )

def randomPlayer1():
    player1 = [ "Callista","Celesta","Caleb","Emmanuel","Christopher","Dad","Mom"]
    return player1[random.randint( 0,6 )]

def randomPlayer2():
    player2 = ["GI 1","GI 2","Sentinal 1","Sentinal 2","Storm Trooper 2", "Storm Trooper 1", "Special OP 1","Elite Soilder 2", "Elite Soilder 1","Special OP 2"]
    return player2[random.randint( 0,9 )]

p1 = Player( randomPlayer1() )
p2 = Player( randomPlayer2() )
print ( "player ", p1.showName() , " starts the game with " , p1.showHP() )
print ( "player ", p2.showName() , " starts the game with " , p2.showHP() )
