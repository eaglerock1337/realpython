from random import random

trials = 10000
prob1 = 0.87
prob2 = 0.65
prob3 = 0.17

def election():
  regions = 0
  regions += prob1 >= random()
  regions += prob2 >= random()
  regions += prob3 >= random()
  return regions >= 2

wins = 0

for i in range(0, trials):
  wins += election()

avg = wins / trials

print("Candidate A will win the election {}% of the time.".format(avg * 100))
print("Candidate B will win the election {}% of the time.".format(100 - (avg * 100)))
