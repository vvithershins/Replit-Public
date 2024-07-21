import random

def get_words_of_length(length, word_list):
    """Get a list of words from the provided list that are of the specified length."""
    return [word for word in word_list if len(word) == length]

def count_matching_letters(secret_word, guessed_word):
    """Count how many letters match in the same position in both words."""
    return sum(1 for s, g in zip(secret_word, guessed_word) if s == g)

def main():
    # A small sample list of words. In a real application, you would use a more extensive word list.
    word_list = ["tree", "bark", "leaf", "rose", "pine", "fern", "moss", "root", "seed", "soil"]

    # Set the secret word
    secret_word = random.choice(word_list)
    word_length = len(secret_word)

    # Generate a list of words of the same length as the secret word
    possible_words = get_words_of_length(word_length, word_list)

    # Ensure the secret word is in the list
    if secret_word not in possible_words:
        possible_words.append(secret_word)

    # Shuffle the list to randomize the order
    random.shuffle(possible_words)

    print("Guess the secret word! Here are your options:")
    for idx, word in enumerate(possible_words, 1):
        print(f"{idx}: {word}")

    while True:
        try:
            guess_index = int(input("\nEnter the number of your guess: ")) - 1
            if guess_index < 0 or guess_index >= len(possible_words):
                print("Invalid input. Please enter a valid number.")
                continue

            guessed_word = possible_words[guess_index]

            if guessed_word == secret_word:
                print("Congratulations! You guessed the correct word!")
                break
            else:
                matching_letters = count_matching_letters(secret_word, guessed_word)
                print(f"{matching_letters} correct letters in the correct position. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()