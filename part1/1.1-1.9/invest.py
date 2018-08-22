def invest(amount, rate, time):
  print("principal amount: ${}".format(amount))
  print("annual rate of return:", str(rate))
  for n in range(1, time+1):
    amount = amount * (1 + rate)
    print("year {}: ${}".format(n, amount))

invest(100, .05, 8)
print()
invest(2000, .025, 5)
