## This is for Lesson 8
import sys

def mul( x, y ):
   z = x * y
   print(z)
   
def add( a, b ):
   c = a + b
   print(c)

def sub( d, e ):
   f = d - e
   print(f)

def div( g, h ):
   i = g / h
   print(i)

def exp( x, y ):
   z = x ** y
   print(z)


try:

   question = input("""What would you like to do?
"add"
"sub"(tract)
"mul"(tiply)
"div"(ide)
"e"(exponent)
"cs"(calculate a score)
""") 

   if question == "add":
      addend = input( 'Please enter an integer addend value : ' )
      addend2 = input( 'Please enter the second integer addend value: ' )

      print(addend, ' + ', addend2, ' = ',add( int(addend), int(addend2) ))
   elif question == "sub":
      print( 'I will subtract any number you want me to.' )
   
      minuen = input( 'Please enter an integer minuen value : ' )
      subtrahend = input( 'Please enter the integer subtrahend value: ' )

      print(minuen, ' - ', subtrahend, ' = ',sub( int(minuen), int(subtrahend) ))
   elif question == "mul":
      print( 'I will multiply any number you want me to.' )
   
      factor = input( 'Please enter an integer factor value : ' )
      factor2 = input( 'Please enter the second integer factor value: ' )

      print(factor, ' * ', factor2, ' = ',mul( int(factor), int(factor2) ))
   elif question == "div":
      print( 'I will divide any number you want me to.' )
   
      dividend = input( 'Please enter a  dividend value : ' )
      divisor = input( 'Please enter the divisor value: ' )

      print(dividend, ' / ', divisor, ' = ',div( int(dividend), int(divisor) ))
   elif question == "cs":
      print( 'I will calculate any score you want me to.' )

   
      sminuen = input( 'Please enter the total number of problems: ' )
      ssubtrahend = input( 'Please enter the number of problems incorrect: ' )
      value = float(sminuen) - float(ssubtrahend)
      result = float(value) / float(sminuen)

      print('Out of a total of ', sminuen, 'problems, you got ', ssubtrahend, ' problems wrong.')
      print("Your score is: ",result)
   elif question == "e":
      base = input( 'Please enter the integer base value : ' )
      exponent = input( 'Please enter the integer exponent value: ' )

      print(base, ' to the power of ', exponent, ' equals ',exp( int(base), int(exponent) ))
   else:
      print('Whats wrong?')


   
except ValueError as e:
   print( 'You did not enter an integer.' )



