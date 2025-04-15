Orig = input("Enter a sentence : ")
newWord = ""
i = -1 # change this to 0 if you want to start with the second letter
for letter in Orig:
  i += 1
  if letter == " ":
    i -=1
  if i % 2 == 0:
    newWord += letter.upper()
  else:
    newWord += letter.lower()
print(newWord)
  
