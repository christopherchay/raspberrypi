import random


knapsack = []
gold = 200
print("Gold: ", gold)
print("Knapsack: ", knapsack)

display = ["knife","bacon","water","axe","sword","pistol","sausage","puppy"]
print(display)

while gold > 0: 
    
    price = random.randint( 1, 100)
    randitem = random.randint( 0,7 )
    if randitem == 0:
        item = "knife"
        print("Your gold: ", gold)
        print( "A ", item, " costs ", price , " gold")
        buy = input('Would you like to buy this item? ')
        if buy == "y":
            gold = gold - price
            knapsack.append(item)
            print("Gold: ", gold)
            print("Knapsack: ", knapsack)
            print("You bought the ", item)
            print('============================')
        else:
            print('You did not buy the item.')
            print('============================')
    elif randitem == 1:
        item = "bacon"
        print("Your gold: ", gold)
        print( "A ", item, " costs ", price , " gold")
        buy = input('Would you like to buy this item? ')
        if buy == "y":
            gold = gold - price
            knapsack.append(item)
            print("Gold: ", gold)
            print("Knapsack: ", knapsack)
            print("You bought the ", item)
            print('============================')
        else:
            print("You did not buy the item")
            print('============================')
    elif randitem == 2:
        item = "water"
        print("Your gold: ", gold)
        print( "A ", item, " costs ", price , " gold")
        buy = input('Would you like to buy this item? ')
        if buy == "y":
            gold = gold - price
            knapsack.append(item)
            print("Gold: ", gold)
            print("Knapsack: ", knapsack)
            print("You bought the ", item)
            print('============================')
        else:
            print("You did not buy the item")
            print('============================')
    elif randitem == 3:
        item = "axe"
        print("Your gold: ", gold)
        print( "A ", item, " costs ", price , " gold")
        buy = input('Would you like to buy this item? ')
        if buy == "y":
            gold = gold - price
            knapsack.append(item)
            print("Gold: ", gold)
            print("Knapsack: ", knapsack)
            print("You bought the ", item)
            print('============================')
        else:
            print("You did not buy the item")
            print('============================')
    elif randitem == 4:
        item = "sword"
        print("Your gold: ", gold)
        print( "A ", item, " costs ", price , " gold")
        buy = input('Would you like to buy this item? ')
        if buy == "y":
            gold = gold - price
            knapsack.append(item)
            print("Gold: ", gold)
            print("Knapsack: ", knapsack)
            print("You bought the ", item)
            print('============================')
        else:
            print("You did not buy the item")
            print('============================')
    elif randitem == 5:
        item = "pistol"
        print("Your gold: ", gold)
        print( "A ", item, " costs ", price , " gold")
        buy = input('Would you like to buy this item? ')
        if buy =="y":
            gold = gold - price
            knapsack.append(item)
            print("Gold: ", gold)
            print("Knapsack: ", knapsack)
            print("You bought the ", item)
            print('============================')
        else:
            print("You did not buy the item")
            print('============================')
    elif randitem == 6:
        item = "sausage"
        print("Your gold: ", gold)
        print( "A ", item, " costs ", price , " gold")
        buy = input('Would you like to buy this item? ')
        if buy == "y":
            gold = gold - price
            knapsack.append(item)
            print("Gold: ", gold)
            print("Knapsack: ", knapsack)
            print("You bought the ", item)
            print('============================')
        else:
            print("You did not buy the item")
            print('============================')
    elif randitem == 7:
        item = "puppy"
        print("Your gold: ", gold)
        print( "A ", item, " costs ", price , " gold")
        buy = input('Would you like to buy this item? ')
        if buy == "y":
            gold = gold - price
            knapsack.append(item)
            print("Gold: ", gold)
            print("Knapsack: ", knapsack)
            print("You bought the ", item)
            print('============================')
        else:
            print("You did not buy the item")
            print('============================')
    else:
        pass

