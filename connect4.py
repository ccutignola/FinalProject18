loop = True #used to run while loop for game
game = 0  #used fo run functions the Start class

grid1 = [0,0,0,0] #first row, bottom
grid2 = [0,0,0,0] #second
grid3 = [0,0,0,0] #third
grid4 = [0,0,0,0] #fourth, top

grids = [grid1,grid2,grid3,grid4]
check = []
user = 1

class fullSlot_error (Exception):
  pass
def winner():
  """Prints this string when someone has won"""
  print ("player "+str(user)+" has won")

#print the grid as it is above
def print_grid():
  """Prints the grid"""
  print ("",grid4,"\n",grid3,"\n",grid2,"\n",grid1)

def pick_user():
  """Determines which user is up to play"""
  global user
  if user < 2:
    user = 2
  else:
    user = 1
  return user

def slot_full():
  """This function determines if the column is full. If it is, the input is invalid and the user has to pick again."""
  while True:
    try:
      if grid4[userInput -1] != 0:
        raise fullSlot_error
      else:
        break
    except fullSlot_error:
      print ("Slot is full!! Try again!!")
      start_round()

def start_round():
  """Asks for the player's choice of column and checks for any invalid inputs"""
  while True:
    try:
      global userInput
      userInput = int(input("Input a slot player "+str(user)+"(1,4)"))
      if userInput < 5 and 0 < userInput:
        return False
      else:
        print ("invalid input".upper())
    #for any inappropriate argument, it will tell the user invalid input
    except ValueError:
      print ("invalid input".upper())

def place_piece():
  """This function checks if the column is full. If it is not, it will insert the player input into that column."""
  for i in range (0,4):
    slot_full()
    if (grids[i][userInput -1] == 0):
      grids [i][userInput - 1] = int(user)
      print_grid()
      break

def check_grid():
  """This function checks each row and column for the combination of 1,1,1,1 or 2,2,2,2. If this is found, the loop would break and it would run the winner() function. If not, the loop would keep running."""
  global loop
  global check
  for i in range(0,4):
    for a in range(0,4):
      check.append(grids[i][a])
    if (check == [1,1,1,1] or check == [2,2,2,2]):
      winner()
      loop = False
      return loop
      break
    else:
      check = []
  for i in range(0,4):
    for a in range(0,4):
      check.append(grids[a][i])
    if (check == [1,1,1,1] or check == [2,2,2,2]):
      winner()
      loop = False
      return loop
      break
    else:
      check = []

def check_empty():
  """This function will check each column and determine if it is full or not"""
  global check
  for i in range (0,4):
    for a in range (0,4):
      check.append(grids[i][a])
  if 0 not in check:
    print ("Full")

def check_diag():
  """This function checks for the combinations of 1,1,1,1 or 2,2,2,2 that are diaganol. If it is found, the loop would stop and it would run the winner() function. If not, the loop would keep running."""
  global loop
  global check
  check = []
  diag = 0
  for i in range (0,4):
    check.append (grids[diag][diag])
    diag = diag +1
    if (check == [1,1,1,1] or check == [2,2,2,2]):
      winner()
      loop = False
      return loop
      break
  check = []
  diag = 3
  diag2 = 0
  for i in range (0,4):
    check.append (grids[diag][diag2])
    if (check == [1,1,1,1] or check == [2,2,2,2]):
      winner()
      loop = False
      return loop
      break

def checks_def():
  """This function will run all the check functions created above to check for a winner and/or an empty column"""
  check_grid()
  check_empty()
  check_diag()

class Start:
  """These functions are used to start the game"""

  def intro(self):
    """Run this to print the intro to the game"""
    print('Welcome to Connect 4!!!!!')

  def rules(self):
    """This tells the players what the rules of the game are"""
    print('Rules: ')
    print('The grid is 4x4'.upper())
    print('Win by connecting four in a row in any direction')



#start the game using the class, Start
game = Start()
game.intro()
game.rules()

#Create a while loop that would run the functions created in the code. When someone wins, they will stop the loop. Otherwise, the loop will continue to run.
while loop == True:
  start_round()
  check_grid()
  place_piece()
  checks_def()
  if loop == False:
      break
  pick_user()