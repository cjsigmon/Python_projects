"""Created by Caleb Sigmon July 4, 2022"""

from random import randint

long = ["Aplomb","Obstreperous", "Ennui",
"Ecumenical",
"Supercilious",
"Amanuensis",
"Flummox",
"Jackdaw",
"Resplendent",
"Ignoramus",
"Curmudgeonliness"]

total_words: int = len(long)
new_word: str = list(long[randint(0, total_words)].upper()) # choose random word, turn to upper case, make into a list
g: int = 6
correct_guess: bool
display = ['_'] * (len(new_word))

while g > 0:
    print(f"You have {g} guesses left")
    correct_guess = False
    print(display)
    j: int = 0
    guess: str = input("What letter would you like to guess? ")
    guess = guess[0].upper() # in case they type more than one letter and to match case
    while j < len(new_word):
        if guess == new_word[j]:
            correct_guess = True
            display[j] = guess
            if display == new_word:
                g = 0
        j+=1
    if correct_guess:
        continue
    g-=1

if correct_guess:
    print("You got it!")
else:
    print("Sorry, you didn't get it.")
print("The word was " + ''.join(new_word))
print("Game Over.")