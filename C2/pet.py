import random
import time

def CareForYourPet():

	print('Hi and welcome to CareForYourPet by PMBD Corporation. ')
	def play():
		name = input('What is your name? ')
		pet = input('What is your pet\'s name?')
		print('''The game is pretty simple. Your job is to make sure your pet is happy and healthy.
		You need to make sure that the pet is not too hungry, if it is too hungry, then it dies and you lose.
		''')
		input('<press enter to continue>')
	
	
		petHealth = 5
		petHappiness = 5
		petHunger = 0
		food = 5
		money = 5
	
		print('Your pet\'s happiness is at ', petHappiness)
		print('Your pet\'s hunger is at ', petHunger)
		print('Your pet\'s health is at ', petHealth)
		print('You have ', money, ' dollars')
		print('Your food is at ', food)
	
		print('''You use 2 dollars to buy 4 food.
	You use 3 food to make your pet's hunger go down 3 and the happiness goes up 2.
	You can make 5 dollars when you make money.
	Your pet's hunger goes up 1 every round.
	You can take your pet to the doctor to make the health go up by 3 but it costs 3 dollars.
	Your pet's health and happiness go down 1 every turn.
	You win the game when the pet's health and happiness are 10 or higher.
	You can play with your pet to increase it's happiness by  3.
	Your pet's health and happiness go down 1 every turn.
	''')
		
		while petHealth > 1 or petHappiness > 1 and petHunger < 10:
			
			action = input(''' You can:
	"f(feed pet)"
	"g(go to doctor)"
	"m(make money)"
	"p(play with pet)"
	"b(buy food)"
	''')
			def result():
				print('Your pet\'s happiness is at ', petHappiness)
				print('Your pet\'s hunger is at ', petHunger)
				print('Your pet\'s health is at ', petHealth)
				print('You have ', money, ' dollars')
				print('Your food is at ', food)
	
			petHunger = petHunger + 1
			petHappiness = petHappiness - 1
			petHealth = petHealth - 1
			if action == "f" and food > 2:
				petHappiness = petHappiness + 2
				petHunger = petHunger - 3
				food = food - 3
				print(name + " you have fed " + pet + ".")
				result()
			elif action == "g" and money > 2:
				petHealth = petHealth + 3
				money = money - 3
				print(name + ", you have taken " + pet + " to the doctor.")
				result()
			elif action == "m":
				money = money + 5
				print(name + ", you made 5 dollars.")
				result()
			elif action == "p":
				petHappiness = petHappiness + 3
				print(name + ", you played with " + pet)
				result()
			elif action == "b" and money > 2:
				food = food + 4
				money = money - 2
				print(name + ", you bought food")
				result()
			else:
				print("You did something wrong") 
				result()
	
			if petHappiness and petHealth > 10 and pethunger < 3:
				print('You win!!' + pet + ' is happy and healthy! Good job!')
				break
			elif petHunger > 10:
				print('I\'m so sorry, '+ name + '.' + pet + ' died of hunger.')
				break
			elif petHealth < 0:
				print('I\'m so sorry, ' + name + '.' + pet + ' died of desease.')
				break
			elif petHappiness < 0 :
				print('I\'m so sorry, ' + name + '.' + pet + ' died of depression.')
			else:
				print('')
	
	
	playAgain = "yes"
	while playAgain == "yes" or playAgain == "y":
		play()
	
		print('Would you like to play again? <type "yes" or "y" if yes>')
		yes = input()	
	