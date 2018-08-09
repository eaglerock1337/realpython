from capitals import capitals_dict
import random

state = random.choice(list(capitals_dict.keys()))
capital = capitals_dict[state]

print("What is the capital of {}?".format(state))

guess = ""

while guess.lower() != capital.lower():
  guess = input("Your answer: ")
  if guess == "quit":
    print("The answer was {}. Goodbye.".format(capital))
    break

if guess.lower() == capital.lower():
  print("Correct!")
