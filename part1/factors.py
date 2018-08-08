num = int(input("Enter a positive integer: "))
for n in range(1, num):
  if num % n == 0:
    print("{} is a divisor of {}".format(n, num))
