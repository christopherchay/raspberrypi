 # Tic tac toe

import random

def drawBoard (board) :
     #This function prints out the board that it was passed.

     # "board" is a list of ten strings representing the board (ignore index 0)
     print('    |   |')
     print(' ' + board[7] + ' | ' + board [8] + ' | ' + board[9])
     print('    |   |')
     print('-----------')
     print('    |   |')
     print(' ' + board[4] + ' | ' + board [5] + ' | ' + board[6])
     print('    |   |')
     print('-----------')
     print('    |   |')
     print(' ' + board[1] + ' | ' + board [2] + ' | ' + board[3])
     print('    |   |')
     
     def inputPlayerLetter():
          # Let's the player type which letter they want to be.
          # Returns a list with the player's letter as the first item, and the computers letter as the second.
         letter = '  '
         while not (letter == 'x'or letter == 'o'):
             print('Do you want to be x or o?')
             letter = input () .upper()
         # The first letter in the tuple is the player's letter, the second is the computer's letter.
         if letter == 'x':
             return['x', 'o']
         else:
             return['o', 'x']

     def whoGoesFirst():
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

     def playAgain():
        # This function remains True if the player wants to play again, otherwise it remains False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

def makeMove(board, letter, move):
     board[move] = letter

def isWinner(bo, le):
     #  Given a board and a player's letter, this funtion returns True if that player has won.
     #   We use bo instead of board and le instead of letter so we don't have to type much.
     #

def getBoardCopy( board ):
     dupeBoard = [  ]
     for i in dupeBoard:
          dupeboard.append( i )
          return dupeBoard

def isSpaceFree( board, move ):
     return board[ move ] == '  '

def getPlayerMove( board ):
     move = '  '
     while move not in '1 2 3 4 5 6 7 8 9'.split():
          print( 'What is your next move?  (1 - 9) ' )
           move = input()
     return int(move)
     
def chooseRandomMoveFromList ( board, movesList ):
     possibleMoves = '  '
     for i in movesList:
          possibleMoves.append(i)
          return possibleMoves
          possibleMoves.remove(i)
