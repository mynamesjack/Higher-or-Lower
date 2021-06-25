from game_data import data
from art import vs
import random

score = 0
is_playing = True

A = random.choice(list(data))

while is_playing == True:
  B = random.choice(list(data))
  print("A.","\n", A["name"],"\n",A["description"],"\n", A["country"])
  print(vs)
  print("B.", "\n", B["name"],"\n",B["description"],"\n", B["country"])
  print("\n")

  answer = input("Who has the higher follower count: 'A' or 'B'?\n")
   
  if A["follower_count"] > B["follower_count"] and answer == 'A':
    score += 1
    print(f"Correct. Your score is now {score}")
    A = A
  
  elif B["follower_count"] > A["follower_count"] and answer == 'B':
    score += 1
    print(f"Correct. Your score is now {score}")
    A = B
  else:
    print(f"Sorry that is incorrect. Your final score is {score}.")
    is_playing = False
