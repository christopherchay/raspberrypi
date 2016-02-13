import random
import time


print('PM CORPORATION PRESENTS:...')
time.sleep(1) 
print('CIV. WARS!!')
time.sleep(1)
print('civWars version 1.2')
time.sleep(1)
#print('NEW CHANGES: better fighting ')
#time.sleep(1)
def civwar():

        myArmy = 15
        invader = 15
	
        time.sleep(1)
        print('Choose a civilisation :')
        you = input('''Greece
America
Korea
Egypt
(default is America)
''')
        if  you == "greece":
                print('You are Greek, and your leader is King Leonidus.')
                civ = "Greece"
                leader = "Leonidus"
        elif you == "korea":
                print('You are Korean, and your leader is Admiral Yi Sun Shin.')
                civ = "Korea"
                leader = "Yi Sun Shin"
        elif you == "america":
                print('You are American, and your leader is President George Washington.')
                civ = "America"
                leader = "George Washington"
        elif you == "egypt":
                print("You are Egyptian, and your leader is Queen Cleopatra.")
                civ = "Egypt"
                leader = "Cleopatra"
        else:
                print('By default, you are American. ')
                civ = "American"
                leader = "George Washington"

        attacker = random.randint(1,9)
        if attacker < 4:
                print('The invaders are the Aztec.')
                enciv = "Aztec"
                enleader = "Zizizangabulubinga"
        elif attacker < 6:
                print('The invaders are the Persians.')
                enciv = "Persia"
                enleader = "King Xerxes"
        elif attacker < 8:
                print('The invaders are the Mongolians.')
                enciv = "Mongolia"
                enleader = "Genghis Kahn"
        else:
                print('The Japanese are invading.')
                envic = "Japan"
                enleader = "Toyomoto Hideyoshi"

        time.sleep(1)
        print(leader + ', You must defend ' + civ + ' from ' + enleader + ', of ' + enciv)
        time.sleep(1)



        print('You and the enemy start with 15 armies each.')
        time.sleep(1)
	
        while  myArmy > 0:
                time.sleep(1)

                dice = random.randint(1,10)
                time.sleep(1)
                if dice < 3:
                        myArmy = myArmy - 2
                        print(enciv, ' has just destroyed 2 armies!!')
                elif dice < 5:
                        myArmy = myArmy - 2
                        invader = invader - 1
                        print(enciv, ' has just destroyed 2 armies!')
                        print(civ + ' has destroyed 1 army!')
                elif dice == 7: 
                        myArmy = myArmy - 2
                        invader = invader - 2
                        print ('Yikes!! ' + civ + ' and ', enciv, ' have lost 2 armies each!!')				
                elif dice < 9:
                        invader = invader - 2
                        myArmy = myArmy -1
                        print(civ + ' has destroyed 2 armies!')
                        print(enciv, ' has destroyed 1 army!')		
                else:
                        invader = invader - 2
                        print('Hoorah!! ' + civ + ' has destroyed 2 armies!!')
					
                print(civ + ' has '  ,myArmy , ' armies left.')
                print(enciv, ' has ' ,invader , ' armies left.')
                print('###################################################')
		

                if myArmy <= 0:
                        print('NOOO! ', enciv, ' has conqured ' + civ + '!!')
                        break
                elif invader <= 0:
                        print('YEESS!!' + civ + ' has repelled the ', enciv, '!!')
                        break

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
        
    civwar()
        
    print('Play again if you wish. ')
    print('Type "yes" or "y" to play again.')
    playAgain = input()

