import random, os


while True:
  games = []
  if os.path.isfile("games.txt"):
    f = open("games.txt","r")
    for line in f:
      games.append(line)
    f.close()
  menu = input("1.(A)dd games\n2.(S)elect random game\n3.(V)iew all games\n4.(D)elete a game\n➡️ ").strip().lower()
  if menu[0] == "a" or menu[0] == "1":
    os.system("clear")
    name = input("Enter the name of the game ")
    syst = input("Which system is it on ")
    game = f"({syst}) | {name}\n"
    if game in games:
      print("game already in games")
    else:
      games.append(game)
      f = open("games.txt", "w")
      for item in games:
        f.write(item)
      f.close()
  elif menu[0] == "s":
    choice = random.choice(games)
    print(choice.replace("\n",""))
    input("Press enter to continue")
    os.system("clear")
  elif menu[0] == "v":
    for game in games:
      print(game)
  elif menu[0] == "d":
    delgame = input("Which game do you want to delete? ")
    for game in games:
      name = game.split("|")[1].strip()
      if delgame == name:
        conf = input("Confirm delete game? ")
        if conf == "y":
          games.remove(game)
          f = open("games.txt", "w")
          for item in games:
            f.write(item)
          f.close()