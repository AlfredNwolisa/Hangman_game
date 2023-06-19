from distutils.command import clean
import random
import hangman_words
import hangman_art
import clear

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#def clear():
    #os.system('cls' if os.name == 'nt' else 'clear')

lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#loop to stop and continue event
while "_" in display:
    guess = input("Guess a letter: ").lower()
    # Clear the screen
    clear()
    if guess in display:
        print()
        print(f"you already guessed the letter {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        print()
        print(f"{guess}, is not part of the word")
        lives -=1
        if lives == 0:
            print()
            print("You lose. You've been hung! ☠️😵")
            break
    print(hangman_art.stages[lives])
while "_" not in display:
    print()
    print(f"You've won fam! The word is {chosen_word}! 🕺⚔️.")
    break
print(hangman_art.stages[lives])