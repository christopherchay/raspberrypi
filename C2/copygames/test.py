def displayMap():
   global square, x
   if xaxis == -1 and yaxis == 1:
      makeBoard( x, square, square, square, square, square, square, square, square )
   elif xaxis == 0 and yaxis == 1:
      makeBoard( square, x, square, square, square, square, square, square, square )
   elif xaxis == 1 and yaxis == 1:
      makeBoard( square, square, x, square, square, square, square, square, square )
   elif xaxis == -1 and yaxis == 0:
      makeBoard( square, square, square, x, square, square, square, square, square )
   elif xaxis == 0 and yaxis == 0:
      makeBoard( square, square, square, square, x, square, square, square, square )
   elif xaxis == 1 and yaxis == 0:
      makeBoard( square, square, square, square, square, x, square, square, square )
   elif xaxis == -1 and yaxis == -1:
      makeBoard( square, square, square, square, square, square, x, square, square )
   elif xaxis == 0 and yaxis == -1:
      makeBoard( square, square, square, square, square, square, square, x, square )
   elif xaxis == 1 and yaxis == -1:
      makeBoard( square, square, square, square, square, square, square, square, x )
   else:
      print('WARNING! SOMETHING WRONG!!')

square = "|  "
x = "x"
divline = "---------------"
pipe = ['|']

def makeBoard( x ):
   print( divline )
   print( '| ' + x[ 0 ] + ' | ' + x[ 1 ] + ' | ' + x[ 2 ] + ' |' )
   print( divline )
   print( '| ' + x[ 3 ] + ' | ' + x[ 4 ] + ' | ' + x[ 5 ] + ' |' )
   print( divline )
   print( '| ' + x[ 6 ] + ' | ' + x[ 7 ] + ' | ' + x[ 8 ] + ' |' )
   print( divline )

position1 = [ x, '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ' ]
position2 = [ '  ', x, '  ', '  ', '  ', '  ', '  ', '  ', '  ' ]
position3 = [ '  ', '  ', x, '  ', '  ', '  ', '  ', '  ', '  ' ]
position4 = [ '  ', '  ', '  ', x, '  ', '  ', '  ', '  ', '  ' ]
position5 = [ '  ', '  ', '  ', '  ', x, '  ', '  ', '  ', '  ' ]
position6 = [ '  ', '  ', '  ', '  ', '  ', x, '  ', '  ', '  ' ]
position7 = [ '  ', '  ', '  ', '  ', '  ', '  ', x, '  ', '  ' ]
position8 = [ '  ', '  ', '  ', '  ', '  ', '  ', '  ', x, '  ' ]
position9 = [ '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', x ]


## Do not use i,t, m , n or any wide letter or thin letter g , f, included

makeBoard( position1 )
