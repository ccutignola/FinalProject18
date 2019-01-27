def start(n=None):
  '''This function starts the game. It allows the user to input the grid size and then create that grid. It uses the functions listed below to run the game. It checks for errors, places the piece, and checks for a winner.'''

  if n is None:
      while True:
        #This allows the user to decide the grid size
        n = int(input('Input the grid size:')

        if n == 0:
          print('cannot be 0'.upper())
          continue
        elif n <= 0:
          print('must be greater than 0'.upper())
          continue
        break

  grids = [[0]*n for _ in range(n)]
  user = 1
  print('Current board:')
  print(*grids, sep='\n')
  while True:
    user_input = get_input(user, grids, n)
    place_piece(user_input, user, grids)
    print('Current board:')
    print(*grids, sep='\n')




def get_input(user, grids, n):
    instr = 'Input a slot player {0} from 1 to {1}: '.format(user, n)
    while True:
        try:
            user_input = int(input(instr))
        except ValueError:
            print('invalid input:', user_input)
            continue
        if 0 > user_input or user_input > n+1:
            print('invalid input:', user_input)
        elif grids[0][user_input-1] != 0:
            print('slot', user_input, 'is full try again')
        else:
            return user_input-1


def place_piece(user_input, user, grids):
    for grid in grids[::-1]:
        if not grid[user_input]:
            grid[user_input] = user
            return


