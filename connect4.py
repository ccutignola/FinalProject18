def intro():
  """Run this to print the intro to the game"""
  print('Welcome to Connect 4!!!!!')

#def get_user_input():
  #user_input = int(input('input a column from 1 - 7'))
  #if 0 > user_input or user_input > 7:
    #print('Invalid! Try again!'.upper())
  #x = print('How many players, 1 or 2?')
  #if x!= 1 or x !=2 :
  #print('Invalid. 1 or 2 !!!!!!!!!!!!'.upper())
DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)

ROWS = 6
COMS = 7

piece_none = ''
one = 'x'
two = 'o'

board = []

def create_board(rows = ROWS, columns = COMS):
  """Creates an empty Connect 4 board."""
  board = []
  for row in range(rows):
    board_row = []
    for column in range(columns):
      board_row.append(piece_none)
    board.append(board_row)
  return board

def copy_board(board):
  """Returns a copy of the created board"""
  rows = len(board)
  columns = len(board[0])
  copied = create_board(rows, columns)

  for row in range(rows):
    for column in range(columns):
      copied[row][column] = board[row][column]
  return copied

def print_board(board):
  """Prints the Connect 4 board"""
  for row in board:
    print('|' + '|'.join(row) + '|')
  return board

def drop_piece(board, column, piece):
  """Allows the user to drop a piece into the board in a specific column"""
  for row in reversed(board):
    if row[column] == piece_none:
      row[column] = piece
      return True
  return False

def find_winner(board, length=4):
  rows = len(board)
  columns = len(board[0])
  for row in range(rows):
    for column in range(columns):
      if board[row][column] == piece_none:
        continue
      if check_piece(board, row, column, length):
        return board[row][column]
  return None

def check_piece(board, row, column, length):
  rows    = len(board)
  columns = len(board[0])

  for dr, dc in DIRECTIONS:
    found_winner = True

    for i in range(1, length):
      r = row + dr*i
      c = column + dc*i

      if r not in range(rows) or c not in range(columns):
        found_winner = False
        break

      if board[r][c] != board[row][column]:
       found_winner = False
       break

    if found_winner:
      return True

  return False
#intro()
create_board()
copy_board(board)
print_board(board)