import os, time, datetime, pytz, random

#Custom Timezone
mytz = pytz.timezone("America/New_York")

#Saving Function
def write():
  f = open("Games.txt", "w")
  f.write(str(games))
  f.close()
  
#Custom Title Function
def CustCap(word):
  if "'" in word:
    new = word.title()
    x = new.split(" ")
    p = ""
    for thing in x:
      if "'" in thing:
        s = thing.split("'")
        y = f"{s[1][0].lower()}" 
        z = f"{s[0]}'{y} {s[1][1:]}"
        thing = z
      p += f"{thing}"
  else:
    p = word
  return p.strip()


# Main Menu
while True:
  games = {}
  if os.path.isfile("Games.txt"):
    r = open("Games.txt","r")
    data = r.read()
    if data != "":
      data = eval(data)
      r.close()
      for key, value in data.items():
        games[key] = value
  menu = ""
  while len(menu) !=1:
    os.system("clear")
    menu = input("\033[92m1.(A)dd a game \n\033[94m2.(S)elect random game \n\033[96m3.(V)iew all games\n\033[31m4.(D)elete a game\n\033[0m➡️ ").strip().upper()

  #Add
  if menu == "A" or menu == "1":
    time.sleep(1)
    os.system("clear")
    addGame = input("Enter the name of the game\n➡️ ")
    addGame = CustCap(addGame)
    syst = input("Which system is it installed on?\n➡️ ").strip().upper()
    prlvl = int(input("Enter priority level low 1-5 high\n➡️ "))
    last = input("When did you last play\n➡️ ")
    if last == "":
      last = "00/00/0000"
    rawtime = datetime.datetime.now(mytz)
    addtime = rawtime.strftime("%m/%d/%Y %H:%M:%S")
    games[addGame] = {"System" : syst, "Priority" : prlvl, "Last Played" : last, "Date Added" : addtime}
    write()

  #Select
  elif menu == "S" or menu == "2":
    def form():
      format = f"""\033[32mGame        : {sel.upper()}
\033[35mSystem      : {games[sel]["System"].upper()}
\033[91mPriority    : {games[sel]["Priority"]}
\033[93mLast Played : {games[sel]["Last Played"]}
\033[36mDate Added  : {games[sel]["Date Added"]}\033[0m"""
      return format 

    def newtime():
      rawtime = datetime.datetime.now(mytz)
      addtime = rawtime.strftime("%m/%d/%Y %H:%M:%S")
      games[sel]["Last Played"] = addtime
    time.sleep(1)
    os.system("clear")
    which = input("1.(R)andom\n2.(P)riority Level\n3.(H)igher than priority level\n4.(W)ithin priority range\n5.(S)ystem\n6.(L)ast played\n➡️ ").strip().upper()
    time.sleep(1)
    os.system("clear")
    if which == "R" or which == "1":
      choices = []
      for game in games:
        choices.append(game)
      sel = random.choice(choices)
      print(form())
      update = input("Update last played to now? ").strip().upper()
      if update[0] == "Y":
        newtime()
        write()
      print()
      
    elif which == "P" or which == "2":
      level = int(input("Which priority level (1-5)? "))
      choices = []
      for game in games:
        if games[game]["Priority"] == level:
          choices.append(game)
      sel = random.choice(choices)
      print(form())
      update = input("Update last played to now? ").strip().upper()
      if update[0] == "Y":
        newtime()
        write()
      print()
      
    elif which == "H" or which == "3":
      level = int(input("Which priority level (1-5)? "))
      choices = []
      for game in games:
        if games[game]["Priority"] >= level:
          choices.append(game)
      sel = random.choice(choices)
      print(form())
      update = input("Update last played to now? ").strip().upper()
      if update[0] == "Y":
        newtime()
        write()
      print()
    
    elif which == "W" or which == "4":
      low = int(input("Enter the low limit "))
      high = int(input("Enter the high limit "))
      choices = []
      for game in games:
        if games[game]["Priority"] >= low and games[game]["Priority"] <= high:
          choices.append(game)
      sel = random.choice(choices)
      print(form())
      update = input("Update last played to now? ").strip().upper()
      if update[0] == "Y":
        newtime()
        write()
      print()

    elif which == "S" or which == "5":
      platf = input("Which system? ").strip().upper()
      choices = []
      for game in games:
        if games[game]["System"].upper() == platf:
          choices.append(game)
      sel = random.choice(choices)
      print(form())
      update = input("Update last played to now? ").strip().upper()
      if update[0] == "Y":
        newtime()
        write()
      print()

    elif which == "L" or which == "6":
      mon,day,year = input("Enter the date mm/dd/yyyy").split("/")
      mon = int(mon)
      day = int(day)
      year = int(year)
      choices = []
      for game in games:
        gyear = int(games[game]["Last Played"][6:10])
        if gyear < year:
          choices.append(game)
        elif gyear >= year:
          gmon = int(games[game]["Last Played"][0:2])
          if gmon < mon:
            choices.append(game)
          elif gmon >= mon:
            gday = int(games[game]["Last Played"][3:5])
            if gday <= day:
              choices.append(game)
          

      if len(choices) > 0:
        sel = random.choice(choices)
        print(form())
        update = input("Update last played to now? ").strip().upper()
        if update[0] == "Y":
          newtime()
          write()
        print()
      else:
        print("No games fit the criteria")
    c = input("Press enter to continue")
    
  #View all 
  elif menu == "V" or menu == "3":
    time.sleep(1)
    os.system("clear")
    for game in games:
      format = f"""\033[32mGame        : {game.capitalize()}
\033[35mSystem      : {games[game]["System"].upper()}
\033[91mPriority    : {games[game]["Priority"]}
\033[93mLast Played : {games[game]["Last Played"]}
\033[36mDate Added  : {games[game]["Date Added"]}\033[0m"""
      print(format)
      print("------------------------------------")
    print()
    c = input("Press enter to continue")

  #Delete
  elif menu == "D" or menu == "4":
    delwhich = input("Which game do you want to delete?")
    if delwhich not in games.keys():
      print("That game does not exist in the data.")
    else:
      confirm = input(f"Are you sure you want to delete {delwhich}? (Y/N)").strip().upper()
      if confirm == "Y":
        del games[delwhich]
        write()
      elif confirm == "N":
        print("Okay, we won't delete it")
    c = input("Press enter to continue")
