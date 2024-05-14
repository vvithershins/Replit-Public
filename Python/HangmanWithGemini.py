from random_word import RandomWords
import google.generativeai as genai
import os ,time


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

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""



genai.configure(api_key=os.environ['api_key'])

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
                              
category = f"""without telling me what this word is : {secret}, in one or two words what category would you say it best fits in"""                    
response = model.generate_content(category)


#print(response.text)

if len(secret) < 7:
  lives = 5
else:
  lives = 6

hangman = """ 🪢
 |
 😢
💪|💪
🦵🦵"""
def showhangman():
  global hangman
  length = len(hangman.strip())
  if lives >= 5:
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
scount = 0
while lives > 0 and getrevealedword().count("_") > 0:
  print(response.text)
  print(lives,"lives")
  showhangman()
  print("guessed letters")
  for letter in sorted(wrong_guesses):
    print(letter, end=" ")
  print()
  print(getrevealedword(),"length = ",len(getrevealedword()))

  guess = input("Guess a letter ").strip().lower()
  while len(guess)!= 1:
    guess = input("please guess a single letter").strip().lower()
  if guess not in correct_guesses and guess not in wrong_guesses:
    if guess in secret:
      print(f"You got {secret.count(guess)} letter(s)")
      correct_guesses.append(guess)
      streak = True
      if streak is True:
        scount +=1
      if scount == 3:
        lives +=1
    elif guess not in secret:
      print("That letters not in the word")
      streak = False
      scount = 0
      lives -=1
      wrong_guesses.append(guess)
    time.sleep(1)
    os.system("clear")
  else:
    print("You already guessed that letter")
    continue
    
else:
  if lives == 0:
    print("🪦")
    print(f"game over, the word was {secret}")
  elif getrevealedword().count("_") == 0:
    print(f"You win you had {lives} lives left, thus you have {lives} points.")




prompt_parts = f"""what is the definition of {secret}?
"""

response = model.generate_content(prompt_parts)
print(secret)
print(response.text)
