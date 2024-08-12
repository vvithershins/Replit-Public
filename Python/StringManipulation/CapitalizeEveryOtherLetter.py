word = input("Enter word > ")
even = ["2","4","6","8","0"]
newword = ""
wordnospaces = word.replace(" ","") 
for i in range(len(wordnospaces)):
  strI = str(i)
  if strI[-1] in even:
    newword += wordnospaces[i].upper()
  else:
    newword += wordnospaces[i]
    
posofspac = []
for i in range(len(word)):
  if word[i] == " ":
    posofspac.append(i)

listword = list(newword)
for spacepos in posofspac:
  listword.insert(spacepos," ")

returnword = "".join(listword)
print(returnword)