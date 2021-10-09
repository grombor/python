# masz błąd, że jak word = 'aaa' i wpiszesz gues = 'a' to od razu wygrywasz

###################
# word definition #
###################

def get_word():
    global word
    word = (input("Welcome in Hangman game !!!\n\nPlease choose the world to guess: ")).lower()
    return word

def print_word(word, guesses):
    for letter in word:
        if letter in guesses:
            print(letter)
        else:
            print("_")

def ask_for_letter():
    global guess
    guess = (input("Quess the letter:  ")).lower()
    return guess

def check_win_conditions(word, guesses):
    for letter in word:
        if letter not in guesses:
            print('kolejna runda')
            return False
    return True


def alert_lose(word):
    print(f"GAME OVER  It was {word}!")

def alert_win():
    print(F"Congratulation you WIN, you found the word: {word} :)")

def step(errors_left):
    if errors_left == 6:
        print()
        print()
        print()
        print()
        print("|")
        print("|")
        print("|")
        print()
    elif errors_left == 5:
        print()
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print()
    elif errors_left == 4:
        print()
        print("________________")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print()
    elif errors_left == 3:
        print()
        print("_________________")
        print("|               |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print()
    elif errors_left == 2:
        print()
        print("_________________")
        print("|               |")
        print("|               @")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print()
    elif errors_left == 1:
        print()
        print("_________________")
        print("|               |")
        print("|               @")
        print("|               |")
        print("|               |")
        print("|")
        print("|")
        print("|")
        print()
    elif errors_left == 0:
        print()
        print("_________________")
        print("|               |")
        print("|               @")
        print("|              /|\\")
        print("|               |")
        print("|              / \\")
        print("|")
        print("|")
        print()


# Initializing global variables

guesses = []
allowed_errors = 7
condition = True

############################
# The start of the program #
############################

word = get_word()
while True:
    print_word(word, guesses)
    guess = ask_for_letter()
    guesses.append(guess)
    if guess not in word:
        allowed_errors -= 1
        if allowed_errors == 0:
            step(allowed_errors)
            alert_lose(word)
            break
        else:
            step(allowed_errors)
    if check_win_conditions(word, guesses):
        alert_win()
        break

##########################
# The end of the program #
##########################