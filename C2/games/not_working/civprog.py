import random

health = 8
list = ["Rome","Egypt","Germany","China","America","Russia"]
print('The Civilisations are: ', list)

while health > 0:
   health =  health - 1
   player = input("Type the name of the player for civilisation: ")

   civ = random.randint(1,6)
   if civ == 1:
      civilisation = "Rome"
      print(player, " is ", civilisation)
      list.remove("Rome")
      print(list)
   elif civ == 2:
      civilisation = "Egypt"
      print(player, " is ", civilisation)
      list.remove("Egypt")
      print(list)
   elif civ == 3:
      civilisation = "America"
      print(player, " is ", civilisation)
      list.remove("America")
      print(list)
   elif civ == 4:
      civilisation = "Germany"
      print(player, " is ", civilisation)
      list.remove("Germany")
      print(list)
   elif civ == 5:
      civilisation = "Russia"
      print(player, " is ", civilisation)
      list.remove("Russia")
      print(list)
   else:
      civilisation = "China"
      print(player, " is ", civilisation)
      list.remove("China")
      print(list)

dice = random.randint(1,4)
if dice == 1:
   print("Callista goes first")
elif dice == 2:
   print("Christopher goes first")
elif dice == 3:
   print("Caleb goes first")
elif dice == 4:
   print("Emmanuel goes first")
else:
   pass

