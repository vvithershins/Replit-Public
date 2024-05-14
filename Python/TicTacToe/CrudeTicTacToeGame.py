import random, os, time
print("Tic-tac-toe game")
time.sleep(1)
board = """1|2|3
-----
4|5|6
-----
7|8|9"""
print(board)

def checkifwin():
  global board
  many = board.count("\n")
  new = board.split("\n")

  for i in range(0,(many -1)):
    if new[i].count("o") == 3:
      print("computer wins")
      exit()
    elif new[i].count("x") == 3:
      print("you win")
      exit()
    i += 1

  copy = board.replace("|", "")
  copy = copy.replace("-", "")
  copy = copy.replace("\n","")
  print(copy)
  if copy[0] == "x":
    if copy[3] =="x":
      if copy[6] == "x":
        print("You win")
        print(board)
        exit()
    elif copy[4] == "x":
      if copy[8] == "x":
        print("You win")
        print(board)
        exit()
        
  elif copy[0] == "o":
    if copy[3] == "o":
      if copy[6] == "o":
        print("I win")
        print(board)
        exit()
    elif copy[4] == "o":
      if copy[8] == "o":
        print("I win")
        print(board)
        exit()
        
  if copy[1] == "x":
    if copy[4] == "x":
      if copy[7] == "x":
        print("You win")
        print(board)
        exit()
  elif copy[1] == "o":
    if copy[4] == "o":
      if copy[7] == "o":
        print("I win")
        print(board)
        exit()
        
  if copy[2] == "x":
    if copy[5] == "x":
      if copy[8] == "x":
        print("You win")
        print(board)
        exit()
    elif copy[4] == "x":
      if copy[6] == "x":
        print("You win")
        print(board)
        exit()
  elif copy[2] == "o":
    if copy[5] == "o":
      if copy[8] == "o":
        print("I win")
        print(board)
        exit()
    elif copy[4] == "o":
      if copy[6] == "o":
        print("I win")
        print(board)
        exit()
checkifwin()


    

cointoss = random.randint(1,2)
hort = input("Heads or tails? (H/T)?").strip().upper()
if hort[0] == "H":
  if cointoss == 1:
    print("Your turn first!")
    playerTurn = True
  elif cointoss == 2:
    print("I go first.")
    playerTurn = False
elif hort[0] == "T":
  if cointoss == 2:
    print("Your turn first!")
    playerTurn = True
  elif cointoss == 1:
    print("I go first.")
    playerTurn = False
time.sleep(2.5)
os.system("clear")
while True:
  count = 0
  for char in board:
    if char.isdigit():
      count +=1
  if count > 0:
    print(board)
    if playerTurn == True:
      choose = input("choose a number")
      while choose not in board and choose.isdigit() is False:
        choose = input("choose a number")  
      if choose in board:
        board = board.replace(choose,"x")
        playerTurn = False
        time.sleep(0.5)
        os.system("clear")
        checkifwin()

        continue
    elif playerTurn == False:
      copy = board.replace("|", "")
      copy = copy.replace("-", "")
      copy = copy.replace("x","")
      copy = copy.replace("o","")
      copy = copy.replace("\n","")
      choice = random.choice(copy)
      board = board.replace(choice,"o")
      time.sleep(0.5)
      os.system("clear")
      playerTurn = True
      checkifwin()
    
      continue
  else:
    print(board)
    checkifwin()
    print("It's a tie.")
 
    break
