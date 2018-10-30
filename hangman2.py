word = "test"

hangman_parts = [" l ", " 0 ", "-l-", "/ \\", "---"]

wrong_guesses=0
while wrong_guesses < len(hangman_parts) :
    guess = input("Please type a guess")
    if guess in word:
        print("Correct")
    else:
        print("Incorrect")
        print(hangman_parts[wrong_guesses])
        wrong_guesses=wrong_guesses+1
        print("you guessed wrong " + str(wrong_guesses))
