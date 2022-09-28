# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments
# The 2048 Game
# import the random module
import random
import copy
# create a board using a list of lists
# create an empty board
print(" "*15," THE 2048 GAME ")
print("\nWelcome to the 2048 game. Your mission is to combine the values in the board which are thesame by merging in different directions until you have at least a 2048.\n \n Follow the instructions below to get started")
rules='''
Each time you will need to type the following characters to move the board in the following directions.

'l' to move Left
'r' to move right
'u' to move up
'd' to move down

You will lose the game if there is no possiblity of moving and the entirer board is filled with numbers

Enjoy!!
'''
print(rules)
boardsize=4
# functin to create the board and display it

def display():
 #check the largest number in the list
  largest_value=0
  for list in board:
    for number in list:
      if number> largest_value:
        largest_value=number
  spaces= len(str(largest_value))      
  for list in board:
    current_row="|"
    for number in list:
      if number==0:
        current_row +=" "*spaces+"|" 
      else:
        current_row += " "*(spaces-len(str(number))) +str(number) +"|"
    print(current_row)    
  print() 

#function to merge left
def merge_rowL(row):
  # place every number on the board to the left as possible
  # j loop shifts the elements 3 times while i loop shifts the elements just once
  for j in range(boardsize-1):
   for i in range(boardsize-1,0,-1):
     if row[i-1]==0:
      row[i-1]=row[i]
      row[i]=0     
# sums the numbers on the board that are thesame
  for i in range(0,boardsize-1):
    if row[i]==row[i+1]:
      row[i]*=2
      row[i+1]=0
  # place the board to the left
  for i in range(boardsize-1,0,-1):
     if row[i-1]==0:
      row[i-1]=row[i]
      row[i]=0     
  
  return row
  # create a function that merges the entirer board left
def merge_left(cur_board):
  for i in range(boardsize):
    cur_board[i]=merge_rowL(cur_board[i])
  return cur_board
# function that reverses the order of one row
def reverse(row): 
  new_board=[]
  for i in range(boardsize-1,-1,-1):
    new_board.append(row[i])
  return new_board 
  # function that merges all the numbers to the right
def merge_right(cur_board): 
  for i in range(boardsize):
    cur_board[i]=reverse(cur_board[i])
    cur_board[i]=merge_rowL(cur_board[i])
    cur_board[i]=reverse(cur_board[i])
  return cur_board
# funtion to transpose the whole board
def transpose(cur_board):
  for j in range(boardsize):
    for i in range(j,boardsize):
      if i != j:
        trans=cur_board[j][i]
        cur_board[j][i]=cur_board[i][j]
        cur_board[i][j]=trans
  return cur_board
  # the function that merges the entire board up
def merge_up(cur_board):
  cur_board=transpose(cur_board)
  cur_board=merge_left(cur_board)
  cur_board=transpose(cur_board)
  return cur_board
# function that merges the entire board down
def merge_down(cur_board):
  cur_board=transpose(cur_board)
  cur_board=merge_right(cur_board)
  cur_board=transpose(cur_board)
  return cur_board
  
# function that chooses a new value from the board
def choose_value():
  if random.randint(1,8)==1:
    return 4
  else:
    return 2
# A  function that adds a value to an empty space in the board the board each time the user the user changes the direction
def add_value():
  row=random.randint(0,boardsize-1)
  column=random.randint(0,boardsize-1)
  while board[row][column] != 0:
    row=random.randint(0,boardsize-1)
    column=random.randint(0,boardsize-1)
  board[row][column] =choose_value() 
# function that test if the user has won
def won():
  for row in board:
    if 2048 in row:
      return True
  return False  
# function that test if the user has lost
def lost():
  temp_board1=copy.deepcopy(board)
  temp_board2=copy.deepcopy(board)
  # test every possible move
  temp_board1=merge_down(temp_board1)
  if temp_board1==temp_board2:
    temp_board1=merge_up(temp_board1)
    if temp_board1==temp_board2:
      temp_board1=merge_left(temp_board1)
      if temp_board1==temp_board2:
        temp_board1=merge_right(temp_board1)
        if temp_board1==temp_board2:
          return True
  return False        
# create an empty board    
board=[]
for i in range(boardsize):
  row=[]
  for j in range(boardsize):
    row.append(0)
  board.append(row)
 
# fills  2 spots on the board with random values
spot=2
while spot>0:
  # place the number in any row or column
  row=random.randint(0,boardsize-1)
  column=random.randint(0,boardsize-1)
  if board[row][column]==0:
    board[row][column]= choose_value()
    spot-=1
display()  
# ask the user to move the board in different directions.
gameover=False
while  not gameover:
  direction=input("which way would you like to move: ")
  # input is valid
  Input=True
  # create a copy of the board
  temp_board=copy.deepcopy(board)
  if direction=="d":
    board=merge_down(board)
  elif direction=="u":
    board=merge_up(board)
  elif direction=="l":
    board=merge_left(board)
  elif direction=="r":
     board=merge_right(board)
  else:
    Input=False
  if Input==False:  
   print("\n.....Enter a valid direction.....\n")
  else:
    if board==temp_board:
      print("Try a different direction")
    else:  
      if won():
        display()
        # if player has won
        print("you won")
        gameover=True
      else:
        add_value()
        display()
        #if player has lost
        if lost():
          print("Sorry you have no more possible moves again you lose!")
          gameover=True
    
