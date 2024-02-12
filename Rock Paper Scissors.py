rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
bool=True
while bool:
  choice=input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n")
  choice1=int(choice)
  if choice1==0:
    print(rock)
  elif choice1==1:
    print(paper)
  elif choice1==2:
    print(scissors)
  print("Computer chose:\n")
  choice2=random.randint(0,2)
  if choice2==0:
    print(rock)
  elif choice2==1:
    print(paper)
  elif choice2==2:
    print(scissors)
  if choice1>choice2:
    if choice1==2 and choice2==0:
      print("You lose")
    else:
      print("You win")
  elif choice1<choice2:
    if choice1==0 and choice2==2:
      print("You win")
    else:
      print("You lose")
  elif choice1==choice2:
    print("It's a draw")
  again=input("Play again? ").lower()
  if again=="no":
    bool=False


