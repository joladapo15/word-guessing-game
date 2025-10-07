import random

word_bank = ["Football", "Soccer","Basketball","Baseball","Tennis"]

word = random.choice(word_bank)

guessedWord = ["_"] * len(word)

attempts = 10

while attempts > 0:
    print("\nCurrent word: " + " ".join(guessedWord))
    guess = input("Guess a letter: ").lower()

    if guess in word.lower():
        for i in range(len(word)):
            if word[i].lower() == guess:
                guessedWord[i] = word[i]
        print("Good try!")
    else:
        attempts -= 1 
        print("Wrong guess! Attempts left:" + str(attempts))

    if "_" not in guessedWord:
        print("\nCONGRATULATIONS!! You guessed the word: " + word)
        break

if attempts == 0 and "_" in guessedWord:
    print("\nYou\'ve run out of attempts! The word was: " + word)
