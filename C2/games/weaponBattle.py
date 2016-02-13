import random
import time

def mortalCombat():

   def holdAxe():
      print('''
            __
           |__|
       0  | 
      /||\/|
     / /\ 
      /  \\
   ''')
   
   def holdSword():
      print('''
           | 
           |
       0 ---
      /||\/|
     / /\ 
      /  \\
      
   ''')
   
   def holdCrossbow():
      print('''
       0___|---  
      /||       
     / /\ 
      /  \\
      
   ''')
   
   def player1():
      fighter1 = input( 'What is your name?' )
      return fighter1
   
   def health1():
      hp1 = 50
      return hp1
   
   def WEAPON1():
      weapon1 = ["Sword","Crossbow","Axe"]
      return weapon1[random.randint(0,2)]
            
   def player2():
      fighter2 = input( 'What is your name?' )
      return fighter2
   
   def health2():
      hp2 = 50
      return hp2
   
   def WEAPON2():
      weapon2 = ["Sword","Crossbow","Axe"]
      return weapon2[random.randint(0,2)]
   
   
   
   p1 = player1()
   p2 = player2()
   
   h1 = health1()
   h2 = health2()
   
   w1 = WEAPON1()
   w2 = WEAPON2()
   
   
   print('NAME: ', p1, ', HP: ', h1, ', WEAPON: ', w1)
   print('NAME: ', p2, ', HP: ', h2, ', WEAPON: ', w2)
   
   input('<press enter to begin the epic battle>')
   
   while h1 > 0 or h2 > 0:
      time.sleep(2)
      
      if w1 == "Sword":
         attack1 = random.randint(1, 11)
         force1 = random.randint(1, 10)
         print( p1, holdSword() )
         print()
      elif w1 == "Axe":
         force1 = random.randint(1, 11) 
         attack1 = random.randint(1, 10)
         print( p1, holdAxe() )
         print()
      elif w1 == "Crossbow":
         attack1 = random.randint(1, 9)
         force1 = random.randint(1, 12)
         print( p1, holdCrossbow() )
         print()
   
      if w2 == "Sword":
         attack2 = random.randint(1, 11)
         force2 = random.randint(1, 10)
         print( p2, holdSword() )
         print()
      elif w2 == "Axe":
         force2 = random.randint(1, 11) 
         attack2 = random.randint(1, 10)
         print( p2, holdAxe() )
         print()
      elif w2 == "Crossbow":
         attack2 = random.randint(1, 9)
         force2 = random.randint(1, 12)
         print( p2, holdCrossbow() )
         print()
   
      def result1():
         if w1 == "Sword":
            resulta1 = random.randint( 0, 2 )
            if  resulta1 == 0:
               print(p1, 'punches', p2 , 'for', force1, 'points')
            elif  resulta1 == 1:
               print(p1, 'stabs with the sword at', p2 , 'for', force1, 'points')
            elif  resulta1 == 2:
               print(p1, 'slashes with the sword at', p2 , 'for', force1, 'points')
            
         elif w1 == "Axe":
            resultb1 = random.randint( 0, 2 )
            if  resultb1 == 0:
               print(p1, 'punches', p2 , 'for', force1, 'points')
            elif  resultb1 == 1:
               print(p1, 'throws the axe at', p2 , 'for', force1, 'points')
            elif  resultb1 == 2:
               print(p1, 'swings with the axe at', p2 , 'for', force1, 'points')
   
         elif w1 == "Crossbow":
            resultc1 = random.randint( 0, 2 )
            if  resultc1 == 0:
               print(p1, 'quickly loads an arrow and shoots', p2 , 'for', force1, 'points')
            elif  resultc1 == 1:
               print(p1, 'bangs the crossbow on', p2 , 'for', force1, 'points')
            elif  resultc1 == 2:
               print(p1, 'punches', p2 , 'for', force1, 'points')
   
      def result2():
         if w2 == "Sword":
            resulta2 = random.randint( 0, 2 )
            if  resulta2 == 0:
               print(p2, 'punches', p1 , 'for', force2, 'points')
            elif  resulta2 == 1:
               print(p2, 'stabs with the sword at', p1 , 'for', force2, 'points')
            elif  resulta2 == 2:
               print(p2, 'slashes with sword at', p1 , 'for', force2, 'points')
            
         elif w2 == "Axe":
            resultb2 = random.randint( 0, 2 )
            if  resultb2 == 0:
               print(p2, 'punches', p1 , 'for', force2, 'points')
            elif  resultb2 == 1:
               print(p2, 'throws the axe at', p1 , 'for', force2, 'points')
            elif  resultb2 == 2:
               print(p2, 'swings with the axe at', p1 , 'for', force2, 'points')
   
         elif w2 == "Crossbow":
            resultc2 = random.randint( 0, 2 )
            if  resultc2 == 0:
               print(p2, 'quickly loads an arrow and shoots', p1 , 'for', force2, 'points')
            elif  resultc2 == 1:
               print(p2, 'bangs the crossbow on', p1 , 'for', force2, 'points')
            elif  resultc2 == 2:
               print(p2, 'punches', p1 , 'for', force2, 'points')
   
   
      if attack1 < 6:
         print(p1, ' missed!!')
      elif attack1 > 5:
         print('POW!!')
         result1()
         h2 = h2 - force1
   
      if attack2 < 6:
         print(p2, ' missed!!')
         print(p1, ':', h1)
         print(p2, ':', h2)
         print('=============================')
      elif attack2 > 5:
         print('BAM!!')
         result2()
         h1 = h1 - force2
         print(p1, ':', h1)
         print(p2, ':', h2)
         print('==================================')
   
         
      if h1 <= 0 or h2 <= 0:
         break
   
   if h1 <= 0 and h2 <= 0:
      print('Both ', p1, ' and ', p2, ' died.')
   elif h1 <= 0:
      print(p1, ' just died!!')
   elif h2 <= 0:
      print(p2, 'just died!!')
   