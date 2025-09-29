#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns True if letter is anywhere in the given word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns True if letter is in the given spot in the word."""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a string:
    - Capital letter if the letter is in the right spot
    - Lowercase letter if the letter is in the word but wrong spot
    - * if the letter is not in the word at all"""
    result = ""
    for i in range(len(myGuess)):
        letter = myGuess[i]
        if inSpot(letter, word, i):
            result += letter.upper()  # correct spot
        elif inWord(letter, word):
            result += letter.lower()  # wrong spot
        else:
            result += "*"             # not in word
    return result

def main():
    # Pick a random word from the list
    with open("words.txt", "r") as wordFile:
        wordList = wordFile.read().splitlines()
    todayWord = random.choice(wordList).lower()

    print("Welcome to Word Game! Guess the 5-letter word.")
    print("Rules: Correct spot = UPPERCASE, wrong spot = lowercase, not in word = *")

    guesses = 6
    for turn in range(guesses):
        guess = input(f"Guess {turn+1}/{guesses}: ").lower()

        # check length
        if len(guess) != len(todayWord):
            print(f"Word must be {len(todayWord)} letters long.")
            continue

        feedback = rateGuess(guess, todayWord)
        print("Result:", feedback)

        if guess == todayWord:
            print("🎉 You got it!")
            break
    else:
        print(f"Out of guesses! The word was: {todayWord}")

if __name__ == "__main__":
    main()
