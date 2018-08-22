while True:
  try:
    num = int(input("Please input an integer: "))
  except ValueError:
    print("try again")
    continue
  break
