from random_word import RandomWords

r = RandomWords()
correct_guesses = []

wrong_guesses = []
secret = r.get_random_word()
def getrevealedword():
  revealedword = ""
  for letter in secret:
    if letter not in correct_guesses:
      revealedword += "_"
    else:
      revealedword += letter
  return revealedword

lives = 5

hangman = """ 🪢
 |
 😢
💪|💪
🦵🦵"""
def showhangman():
  global hangman
  length = len(hangman.strip())
  if lives == 5:
    print(hangman)
  elif lives == 4:
    newhangman = hangman.strip()[0:length-1]
    print(newhangman)
  elif lives == 3:
    newhangman = hangman.strip()[0:length-2]
    print(newhangman)
  elif lives == 2:
    newhangman = hangman.strip()[0:length-4]
    print(newhangman)
  elif lives == 1:
    newhangman = hangman.strip()[0:length-6]
    print(newhangman,"|")

while lives > 0 and getrevealedword().count("_") > 0:
  print(lives,"lives")
  showhangman()
  print(getrevealedword())
  guess = input("Guess a letter ")
  if guess not in correct_guesses and guess not in wrong_guesses:
    if guess in secret:
      print(f"You got {secret.count(guess)} letter(s)")
      correct_guesses.append(guess)
    elif guess not in secret:
      print("That letters not in the word")
      lives -=1
      wrong_guesses.append(guess)
  else:
    print("You already guessed that letter")
    continue
else:
  if lives == 0:
    print("🪦")
    print(f"game over, the word was {secret}")
  elif getrevealedword().count("_") == 0:
    print(f"You win you had {lives} lives left, thus you have {lives} points.")
