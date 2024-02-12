#Step 3

import random
import hangman_words
import hangman_art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
from replit import clear
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(logo)
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
lives=6
end=True
while end==True and lives>0:
  guess = input("Guess a letter: ").lower()
  clear()
  for position in range(word_length):
    letter = chosen_word[position]
    if display[position]==guess:
      print("You have already guessed this letter")
    if letter == guess:
        display[position] = letter
  if "_" not in display:
    print("You win.")
    end=False
  if guess not in chosen_word:
      lives-=1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
  if lives<1:
    print(f"You lose, the word was {chosen_word}")
  print(display)
  print(stages[lives])
