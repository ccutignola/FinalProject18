def intro():
  """Run this to print the intro to the game"""
  print('Welcome to Connect 4!!!!!')

def get_user_input():
  user_input = int(input('input a column from 1 - 7'))
  if 0 > user_input or user_input > 7:
    print('Invalid! Try again!'.upper())
  #x = print('How many players, 1 or 2?')
  #if x!= 1 or x !=2 :
  #print('Invalid. 1 or 2 !!!!!!!!!!!!'.upper())


def create_board():
  row1= [0,0,0,0,0,0,0]
  row2 = [0,0,0,0,0,0,0]
  row3 = [0,0,0,0,0,0,0]
  row4 = [0,0,0,0,0,0,0]
  row5 = [0,0,0,0,0,0,0]
  row6 = [0,0,0,0,0,0,0]

  board = print ("",row6,"\n",row5,"\n",row4,"\n",row3,"\n",row2,"\n",row1)
  return board
board = create_board



create_board()
#intro()