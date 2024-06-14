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
    t = ""
    TAGS = []
    while t != "DONE":
      t = input("Enter a tag or enter DONE to finish. ")
      if t != "DONE":
        TAGS.append(t)
    games[addGame] = {"System" : syst, "Priority" : prlvl, "Last Played" : last, "Date Added" : addtime, "Tags" : TAGS}
    write()

  #Select
  elif menu == "S" or menu == "2":
    def form():
      format = f"""\033[32mGame        : {sel}
\033[35mSystem      : {games[sel]["System"].upper()}
\033[91mPriority    : {games[sel]["Priority"]}
\033[93mLast Played : {games[sel]["Last Played"]}
\033[36mDate Added  : {games[sel]["Date Added"]}\033[0m
Tags        : {games[sel]["Tags"]}"""
      return format 

    def newtime():
      rawtime = datetime.datetime.now(mytz)
      addtime = rawtime.strftime("%m/%d/%Y %H:%M:%S")
      games[sel]["Last Played"] = addtime
