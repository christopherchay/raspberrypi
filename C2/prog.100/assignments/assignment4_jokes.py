## This is a joke program.
import random
import sys

## Create a variety of jokes with my own function
def generateJoke():
   jokes = [ "What do you get when you cross a Guido Van Rossum with a flying circus? ",
             "What do dentist's call a blackhole? ",
             "What did the lightbulb say to the other lightbulb? ",
             "How do you know if an elephant has been in your house? "]
   return jokes[ random.randint( 0, 3 ) ]

# Now this will continuously generate jokes.

print( 'Type "q" to quit at any time during the program.' )

while True:
   joke = generateJoke()
   z = input(  )
   if z == "q":
      sys.exit()
   print()
   print( joke )

   if "Guido" in joke:
      answer = input( '''"a". Cobra
"b". Flying Rossum
"c". Python
''' )
      if answer == "c":
         print( 'Python!!, Correct' )
      elif answer == "b":
         print( 'That\'s hillarious!!' )
      else:
         print( 'Nope, not quite.' )

   elif "lightbulb" in joke:
      answer = input('''"a". Watt is going on?
"b". Watcha doin' ?
"c". Your bill is overdue!!
''')
      if answer == "a":
         print( 'You guessed it!!' )
      else:
         print( 'That was pretty close, I assure you.' )

   elif "elephant" in joke:
      answer = input('''"a". When your roof is gone.
"b". When you have to replace your bed.
"c". When you hear trumpting in the distance.
''')
      if answer == "a" or answer == "b":
         print( 'Lol, that\'s right!!' )
      else:
         print( 'Sorry, maybe next time.')
         
   elif "dentist" in joke:
      answer = input('''"a". A cavity!!
"b". A sign for a root-canal'
"c". Bad breath.
''')
      if answer == "a":
         print( 'Correct!!' )
      else:
         print( 'You were very close.')
