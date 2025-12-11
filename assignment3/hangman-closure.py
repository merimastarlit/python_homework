
#Task 4

def make_hangman(secret_word):
    #empty list to store guessed letters
    guesses = []
    #the closure function that will process the guesses
    def hangman_closure(letter):
        guesses.append(letter)
        for letter in secret_word:
            if letter in guesses:
                print(letter, end="")
            elif letter not in guesses:
                print("_", end="")
        #check if all letters have been guessed
        if all(letter in guesses for letter in secret_word):
            return True
        else:
            return False

    return hangman_closure

#using the closure
the_secret = make_hangman("education")
done = False
while not done:
    main_input = input("Guess a letter: ")
    done = the_secret(main_input)

if done:
    print("\nYou guessted the word!")





