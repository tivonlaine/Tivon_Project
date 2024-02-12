############### Blackjack Project #####################


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

from art import logo
import random
def generatecards():
  card=random.choice(cards)
  return card
def computerscore(computercards):
  compsum=0
  for i in computercards:
    if i==11 and compsum>10:
      i=1
    compsum+=i
  return compsum
def playerscore(playercards):
  playersum=0
  for i in playercards:
    if i==11 and playersum>10:
      i=1
    playersum+=i
  return playersum
def blackjack():
  print(logo)
  playercards=[generatecards(), generatecards()]
  computercards=[generatecards(), generatecards()]
  print(f"Your cards: {playercards}, current score {playerscore(playercards)}")
  print(f"Computer's first card: {computercards[0]}")
  while computerscore(computercards)<17:
    computercards.append(generatecards())

  another=input("Type 'y' to get another card, type 'n' to pass: ")
  if another=="y":
    playercards.append(generatecards())
    print(f"Your cards: {playercards}, current score: {playerscore(playercards)}")
    print(f"Computer's first card: {computercards[0]}")
  print(f"Your final hand: {playercards}, final score: {playerscore(playercards)}")
  print(f"Computer's final hand: {computercards}, final score: {computerscore(computercards)}")
  if playerscore(playercards)==computerscore(computercards):
    print("You tied")
  if playerscore(playercards)>21:
    print("Game Over: You Lose")
    return
  if playerscore(playercards)>computerscore(computercards) or computerscore(computercards)>21:
    print("You Win")
  elif computerscore(computercards)>playerscore(playercards):
    print("You Lose")
  start=input("Do you want to play a game of BlackJack? ")
  if start=="yes":
    blackjack()
blackjack()


