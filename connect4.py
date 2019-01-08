import numpy as np

def intro():
  """Run this to print the intro to the game"""
  print('Welcome to Connect 4!!!!!')

def start():
  """Run this to start the game"""
  #x = print('How many players, 1 or 2?')
  #if x!= 1 or x !=2 :
  #print('Invalid. 1 or 2 !!!!!!!!!!!!'.upper())


def create_board():
  board = np.zeros((6, 7))
  return board


board = create_board
print(board)

#intro()
#start()