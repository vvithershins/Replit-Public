import Foundation

func generateRandomNumber(maxNumber: Int) -> Int {
    return Int.random(in: 1...maxNumber)
}

func playGame(maxNumber: Int) {
    let randomNumber = generateRandomNumber(maxNumber: maxNumber)
    print("Welcome to the number guessing game!")
    print("I have chosen a random number between 1 and \(maxNumber).")
    print("Can you guess it?")
    
    var guessCount = 0
    var guessedCorrectly = false
    
    while !guessedCorrectly {
        guard let guess = Int(readLine()!) else {
            print("Invalid input. Please enter a valid number.")
            continue
        }
        
        guessCount += 1
        
        if guess == randomNumber {
            guessedCorrectly = true
            print("Congratulations! You guessed the number \(randomNumber) in \(guessCount) tries.")
        } else if guess < randomNumber {
            print("Too low. Try again.")
        } else {
            print("Too high. Try again.")
        }
    }
}

print("What is the maximum number you want to guess?")
guard let maxNumber = Int(readLine()!) else {
    print("Invalid input. Please enter a valid number.")
    exit(1)
}

playGame(maxNumber: maxNumber)
