import time

word = "python"
progress = ["?", "?", "?", "?", "?", "?"]
guesses = 0
right_result = 0
wrong_result = 10


def initial_diagram():
    print("|--------|        ")
    print("|                 ")
    print("|                 ")
    print("|                 ")
    print("|_________________")


def diagram():
    if guesses == 1:
        print("|--------|        ")
        print("|        0        ")
        print("|                 ")
        print("|                 ")
        print("|_________________")
    elif guesses == 2:
        print("|--------|        ")
        print("|        0        ")
        print("|        |        ")
        print("|                 ")
        print("|_________________")
    elif guesses == 3:
        print("|--------|        ")
        print("|        0        ")
        print("|        |-       ")
        print("|                 ")
        print("|_________________")
    elif guesses == 4:
        print("|--------|        ")
        print("|        0        ")
        print("|        |--      ")
        print("|                 ")
        print("|_________________")
    elif guesses == 5:
        print("|--------|        ")
        print("|        0        ")
        print("|       -|--      ")
        print("|                 ")
        print("|_________________")
    elif guesses == 6:
        print("|--------|        ")
        print("|        0        ")
        print("|      --|--      ")
        print("|                 ")
        print("|_________________")
    elif guesses == 7:
        print("|--------|        ")
        print("|        0        ")
        print("|      --|--      ")
        print("|       /         ")
        print("|_________________")
    else:
        print("|--------|        ")
        print("|        0        ")
        print("|      --|--      ")
        print("|       / \       ")
        print("|_________________")


def progress_status():
    if guesses == 8:
        print(" ")
        time.sleep(1)
        print("Although you have used up all of your guesses, you can take one final guess at what the word is...")
        print(" ")
        time.sleep(1)
        final_guess = input("Final guess: ")
        final_guess = final_guess.lower()
        if final_guess == word:
            time.sleep(1)
            print(" ")
            print("That is correct!")
            time.sleep(1)
            print(" ")
            print("You win!")
            exit()
        else:
            print(" ")
            time.sleep(1)
            print("You've used up all your guesses, and have been hung!")
            time.sleep(1)
            print(" ")
            print("You lose!")
    else:
        time.sleep(1)
        print(" ")
        print("You still have", 8 - guesses, "guesses left, keep going!")


print("Welcome to Hangman!")
time.sleep(2)
print("You will have 8 guesses, with which you can guess a letter that is in a secret word.")
time.sleep(2)
print("If you use up all 8 before you guess the word you lose!")
time.sleep(2)
print("Good luck!")
time.sleep(2)
print(" ")
print("Your progress will be tracked here: ")
print(progress)
initial_diagram()


while guesses <= 7:
    print(" ")
    guesses = guesses + 1
    time.sleep(1)
    current_guess = input("Guess a letter: ")
    current_guess = current_guess.lower()
    time.sleep(1)
    if current_guess in progress:
        time.sleep(1)
        print("You've already guessed that letter.")
        time.sleep(1)
        print("That counts as one of your guesses!")
        time.sleep(1)
        print(" ")
        print(progress)
        diagram()
        progress_status()
    elif current_guess in word:
        print("That letter is in the word!")
        letter_index = int(word.index(current_guess))
        progress[letter_index] = current_guess
        time.sleep(1)
        print(" ")
        print(progress)
        diagram()
        progress_status()
        if progress == ["p", "y", "t", "h", "o", "n"]:
            print("Congratulations!")
            time.sleep(1)
            print("You have successfully guessed the word, well done.")
            time.sleep(1)
            print(" ")
            print("The word was PYTHON!")
            quit()
        elif guesses == 8:
            quit()
        else:
            time.sleep(1)
            print(" ")
            print("You haven't got the full word yet, keep going")
    else:
        print("Unlucky, that letter is not in the word!")
        print(" ")
        time.sleep(1)
        print(progress)
        diagram()
        time.sleep(1)
        print(" ")
        progress_status()
