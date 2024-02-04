from art import logo
from art import vs
from game_data import data
import random
from replit import clear

def person():
  person=random.choice(data)
  name=person['name']
  desc=person['description']
  country=person['country']
  followers=person['follower_count']
  return name, desc, country, followers
  
#print(logo)
bool=True
score=0
name1, desc1, country1, followers1=person()
print(logo)
while bool:
  name2, desc2, country2, followers2=person()
  print(f"Compare A: {name1}, a {desc1} from {country1}    {followers1}")
  print(vs)
  print(f"Against B: {name2}, a {desc2} from {country2}  {followers2}")
  guess=input("Who has more followers? Type 'A' or 'B': ")
  clear()
  print(logo)
  if (followers1>followers2 and guess=="A") or (followers2>followers1 and guess=="B"):
    score+=1
    print(f"You're right! Current score: {score}")
  else: 
    print(f"Sorry, that's wrong. Final score: {score}")
    bool=False
    break
  name1=name2
  desc1=desc2
  country1=country2
  followers1=followers2
 

