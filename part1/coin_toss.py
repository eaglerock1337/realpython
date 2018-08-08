from random import randint

trials = 10000

def toss():
  first = randint(0, 1)
  tosses = 1
  while True:
    tosses += 1
    if first != randint(0, 1):
      break
  return tosses
  
flips = 0

for i in range(0, trials):
  flips += toss()

print("The average number of flips is {}.".format(flips / trials))
