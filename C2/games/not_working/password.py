## password emulator:
import random
import sys

def passwordGame():
   turn = 5

   def hiddenPassword():
      password = ["spiderman","captainamerica","blackcat", "invisiblewoman"]
      return password[random.randint(0,3)]

   password = hiddenPassword()
   user = input('Username:  ')
   print('password hint: A super hero or heroine')

   while True:
      print('Tries left(before computer locks out): ', turn)
      entry = input('Password: ')
      if entry == password:
         print('Welcome, ' + user + '.')
         print('Loading your personal settings.......')
         break
      else:
         print('The password is incorrect.')
         turn = turn - 1
         if turn == 0:
            break
   if turn == 0:
      print('I\'m sorry ' + user + ', but you have been locked out. :(')

print('Welcome to Anyone\'s Computer!!')
passwordGame()


