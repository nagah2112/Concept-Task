#["nagah" ,"ramadan"]  "nagah" "ganah" gahna nagah
import random

def scramble_word(word):
    return ''.join(random.sample(word , len(word))) #"nagah" -> "ganah"

def game():
    words = ["apple" ,"banana" , "peach" ,"grape" , "cherry"]
     
    fact_word = random.choice(words) # "ganah"

    scrambled_word = scramble_word(fact_word)

    print("Welcome to the Word Scramble Game!")
    print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
    print("You have 5 attempts.")

    geuss_cntr = 5

    while geuss_cntr>0:
        guess = input("enter your guess: ").strip().lower()
        if not guess:
            print("Invalid input! Please enter a word.")
        
        if guess == fact_word:
            print("Congratulations! You guessed the correct word!")
        else:
            geuss_cntr -=1
            if geuss_cntr>0:
                print(f"Incorrect! Try again. You have {geuss_cntr} attempts left.")
            else:
                print(f"You're out of attempts! The correct word was: {fact_word}")


game()