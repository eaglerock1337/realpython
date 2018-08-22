from random import randint

trials = 10000
add = 0
for i in range(0, trials):
  add += randint(1, 6)
avg = add / float(trials)
print("The average die roll after {} rolls is {}.".format(trials, avg))
