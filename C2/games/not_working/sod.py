import random
import time
import sys

hp = 10

def displayInventory():
   print('NAME:', name)
   print('AGE:', age)
   print('GENDER:', gender)
   print('HP:', hp)
   print('Weapon:', weapon)
   print('AMMO:', ammo)
   print('  ')
   

name = input("What is your name? ")
age = input("How old are you? ")
gender = input("And finally, what is your gender? ")

print('Name:',name, ',Age:', age, ',Gender:', gender)
choice = input('Are you satisfied with the results? (type n or on) to male changes or press enter to continue.')
if choice == "no" or choice == "n":
   while 1 ==1:
      choice1 = input('''What would you like to change?
name
age
gender
(or type z to quit)
''')
      if choice1 == "name":
         name = input('Please type a new name: ')
         print('Name:',name, ',Age:', age, ',Gender:', gender)
      elif choice1 == "age":
         age = input('Please type a new age: ')
         print('Name:',name, ',Age:', age, ',Gender:', gender)
      elif choice1 == "gender":
         gender = input('Please type a new gender: ')
         print('Name:',name, ',Age:', age, ',Gender:', gender)
      elif choice1 == "z":
         break

print('{}, you wake up in a musty old room. It\'s dark and you don\'t remember anything...' .format(name))
print('All you find on you is your old nerf gun the........')
weapon = random.randint(0,2)
if weapon == 1:
   weapon = "Hammershot"
   print('........', weapon)
   ammo = 5
elif weapon == 2:
   weapon = "Strongarm"
   print('........', weapon)
   ammo = 6
else:
   weapon = "Roughcut"
   print('........', weapon)
   ammo = 8

displayInventory()

print('')
event = input('You were unable to remember anything of the past so you can either: "l"leave the room, "e"explore a bit ')
if event == "e":
   print('You stumble and trip as you look for the wall. It is pretty dark so you switch on a light. The room is empty, except for debris and a box of 25 nerf darts. You pick it up.')
   ammo = ammo + 25
   print('Seeing that there is nothing left, you open the door to the outside...... ')
   input('<press enter to continue>')
else:
   print('You open the door that leads outside......')
   input('<press enter to continue>')

print('To your suprise, it leads to a snowy street with blustering winds. Fortunately, you have warm clothes. Suddenly, you see a man run in your direction.')
event2 = input('Do you "c"confront him or "h"hide in an alley?')
if event2 == "c":
   print('''You: Excuse me, sir!
Man [breathless]: W-w-hat d-do you need? 
you: Are you okay?
man: No! I'm  running from a 6 ft tall robot.
you: Say what?
man: Yes, a Robot. The robot apocalypse is here, and you'd better run. I gotta go home to my wife.
you: What's your name?
man: David Dimond.
You: I'm {}.
man: Well it's nice meeting you.
He runs off and you hide behind a building.
''' .format(name))
   input('<press enter to continue>')
else:
   print('You cower into an alleyway and watch the man run past....')
   input('<press enter to continue>')

print('To your suprise, you see a giant robot walking through the streets. The sight alone makes you tremble, and you give a gasp.')
input('<press enter to continue>')
print('As you silently watch, the thought of running away came to your mind. You decided against it, as the snow was 6 inches deep.')

event3 = input('By the merest chance, the robot spots you and walks rather quickly in your direction. Do you "s" shoot it or "r" runaway?')
print('  ')
if event3 == "s":
   print('You whip out your {} and take aim. I\'m probably being an idiot. You think. You shoot the robots arm, making it fall off.' .format(weapon))
   print('The robot gives a roar like a lion and jumps at you making your heat jump into your mouth. You shoot monster\s head while rolling backwards.')
   input('<press enter to continue>')
   print('After you regain your composure, you think, Man, these nerf guns are pretty nifty. You stumble away , your legs stiff and shaky from the scare....')
   ammo = ammo - 3
   displayInventory
   print('''You meet a girl coming from the opposite direction.
girl: Are you okay?
you:Yeah, I'm fine.
girl: I'm Juna Evans.
you: And I'm {}, pleasure meeting you.
girl: The pleasure is mine.
Suddenly, the ground quakes nearby.
girl: We had better get to a safe place.
You nod and follow her out of the alley.
''' .format(name))
   displayInventory()
else:
   print('''You run away with all your might but the robot runs after you. After running for about 5 minutes, you start to get winded.
Running in the snow is no easy task, especially when you are filled with fear. The robot suddenly grabs and pinches your shoulder.
You give a cry of pain as the robot grips your other shoulder and starts to lift up up in the air.
As you start to lose conciousness, you faintly see a girl shooting at the robot...
''')
   input('<press enter to continue>')
   print('''The next thing you know, the girl is hovering you making sure you are okay.
girl: Are you all right?
you: Yes, I think so....
girl: I'm glad. I came just in time. I'm Juna Evans.
you: I'm {}, thank you.
girl: Oh that's all right, if you feel good enough, stand up, We have to move on to a safer place.
you: Okay, let's go.
''' .format(name))
   hp = hp - 1
   displayInventory()

print('''You and Juna walk out of the alley and run into a young man standing gaurd in front of a building.
man: Hey Juna, find someone?
Juna: Yes, Krayle. This is {}.
Krayle: Hi {}.
you: Hi Krayle. Ummm..... What's going on?
Krayle: Generally, getting out of the city. Specifically, Well, We're just getting supples. Melvin is around here somewhere.
Melvin: Hey, did you call me, Kray?
Krayle: No, but I'm glad you came. Meet {}.
Melvin: Hi {}, I'm Melvin.
Juna: It's all great to get to know each other, but I think we should get to a safe place so we can avoid all opposition.
Melvin: Right, Juna. Kryale, let's go to the library.
Krayle: OKay, Let's go guys......
''' .format(name))
input('<press enter to continue>')
print('''You notice that Krayle is carrying a Maverick, Juna is armed with a Retaliator, and Melvin has a Centurion.
You soon arrive at the library and set up shop there.
Krayle: Okay, let's split up. One group will get food, the other will get tools or supplies. I'm gonna get supplies.  {}, you can choose someone to go with to get food.
''' .format(name))



sys.exit()
